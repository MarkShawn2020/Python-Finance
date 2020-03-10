# -*- coding: utf-8 -*-
import scrapy
import json


class CompanySpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['linkedin.com']

    companies_id_dict = {
        1038: 'Deloitte',
        3014: 'Huawei Technology',
        2114: 'Bain & Company'
    }

    N_pp = 40

    def gen_search_url(self, company_id, start, count=N_pp, regions='cn%3A0'):
        return '''https://www.linkedin.com/voyager/api/search/blended?count={count}&filters=List(currentCompany-%3E{companies},geoRegion-%3E{regions},resultType-%3EPEOPLE)&origin=FACETED_SEARCH&q=all&queryContext=List(spellCorrectionEnabled-%3Etrue,relatedSearchesEnabled-%3Etrue)&start={start}'''.format(
            start=start,
            count=count,
            companies=company_id,
            regions=regions,
        )

    def start_requests(self):
        company_id = '1038'
        meta = {'company_id': company_id, 'start': 0}
        url_to_search = self.gen_search_url(**meta)
        print(url_to_search)

        yield scrapy.Request(url_to_search, meta=meta)

    def parse(self, response):
        j = json.loads(response.text)
        meta_data = j['data']['metadata']
        total_members = meta_data['totalResultCount']
        response.meta['start'] += self.N_pp
        self.logger.info({'TotalMembers': total_members, 'NowFinished': response.meta['start']})

        for element in j['data']['elements'][-1]['elements']: # -1的用意在于，第二页相较于第一页缺少了第一个列表键
            try:
                public_identifier = element['publicIdentifier']
                element['public_url'] = 'https://www.linkedin.com/in/{}/'.format(public_identifier)
                yield element
            except KeyError as e:
                self.logger.warning('No Public Identifier for this item {}')
                pass

        if meta_data['numVisibleResults'] < self.N_pp:
            self.logger.info('Finished Company {}'.format(response.meta['company_id']))
        else:
            next_url = self.gen_search_url(response.meta['company_id'], response.meta['start'])
            yield scrapy.Request(next_url, meta=response.meta, callback=self.parse)

