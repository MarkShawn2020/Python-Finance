from bs4 import BeautifulSoup
from bs4 import element


soup_text = '''<?xml version="1.0" encoding="utf-8"?>
<UserAuthResponse xmlns="http://schemas.datacontract.org/2004/07/Factminr.WebApi.Module.Response.User" xmlns:i="http://www.w3.org/2001/XMLSchema-instance"><Email i:nil="true"/><Expand>0</Expand><Folders
i:nil="true"/><LandingPage>0</LandingPage><NickName i:nil="true"/><PageSize>0</PageSize><Phone i:nil="true"/><ResponseCode>402</ResponseCode><ResponseMessage>incorrect username/password</ResponseMessage>
<Role i:nil="true"/><Sort>0</Sort><Tag i:nil="true"/><Token i:nil="true"/><Uid i:nil="true"/><WxStatus>0</WxStatus></UserAuthResponse>'''

soup = BeautifulSoup(soup_text, 'xml')


def tag_children(tag, i):
    if not isinstance(tag, element.NavigableString):
        if len(tag.find_all()):
            print('[{0}] {1:20}{2:30}'.format(i, tag.name, str(type(tag))))
            for tag_child in tag.children:
                tag_children(tag_child, i+1)
        else:
            print('[{0}] {1:20}{2:30}:{3}'.format(i, tag.name, str(type(tag)), tag.string))
    else:
        print('[{0}] {1}\t\t\t{2}'.format(i, tag.parent.name, tag))


def get_soup_structure(soup, length=20):
    str_print = ''
    for node in soup.descendants:
        if not isinstance(node, element.NavigableString):
            if node.find() is None:
                path = [i.name[:length] for i in node.parents][-2::-1]
                path.append(str({node.name: node.string}))
                for i, j in enumerate(path):
                    str_print += '{0}: {1:{2}}\t'.format(i, j, length)
                str_print += '\n'
    return str_print


print(get_soup_structure(soup))

