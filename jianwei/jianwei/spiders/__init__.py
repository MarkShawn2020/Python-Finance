# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


# def convert_fromdata(self, data_raw, colon_or_not=True, token=None, ):
#     data_dict = {}
#     for i in data_raw.splitlines():
#         if colon_or_not:
#             data_dict.update({i.split(': ', 1)[0].strip(): i.split(': ', 1)[1].strip()})
#         else:
#             data_dict.update({i.split('\t ', 1)[0].strip(): i.split('\t ', 1)[1].strip()})
#
#     if token:
#         data_dict.update({'token': token})
#     pprint(data_dict)
#     return data_dict