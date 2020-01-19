
import os
import re
from urllib.parse import unquote

from qiniu import Auth, put_file


"""
1. 打开.md文件（由于Github无法识别断开的链接，因此文件名不要断开的好）
2. 替换.md文件中所有的图片链接
    1. 匹配出.md文件中的路径，一般就是relative_source_dir_path + file_name
        1. 如果是本地的话，直接open打开即可（比如Typora）
        2. 如果是在线的话，需要用cookie访问，并保存到本地（比如为知）
        3. 由于七牛云的api基于本地文件路径，所以需要建立一个转换函数
    2. 将图片上传到七牛云，并返回七牛云反馈的图片网址
    3. 将返回的图片网址插入到原.md链接处
3. 保存成另一份.md文件
"""



def img_path_online2local(img_path: str) -> str:
    """
    图片的在线地址解析、下载到本地后，返回本地真实地址
    :param img_path:
    :return:
    """
    # 如果是为知笔记的话
    pass
    return img_path


def get_online_img_path(img_abs_path, md_file_path):
    from settings import AK, SK, DOMAIN, BUCKET_NAME
    q = Auth(AK, SK)

    md_dir_path = os.path.dirname(md_file_path)
    # 先将md文件中的图片链接，解码成正常的utf-8格式，比如typora中的中文链接是被编码的
    # 且编码可能并不完全，比如 + 号就没转码
    # 所以解码会比编码方便
    img_abs_path = os.path.join(md_dir_path, unquote(img_abs_path))
    if os.path.exists(img_abs_path):
        # 如果本地存在图片，且是相对路径，就直接返回图片的相对路径；绝对路径就返回最后两段路径
        print("Find local img path: {}".format(img_abs_path))
        # 网址链接是支持含有空格、加号等的，空格会自动进行转化成%20
        # 有意思的是 + 号是不转化的，但是urllib.parse.quote()函数却把它转换成了%2B
        online_img_path = "/".join(img_abs_path.replace("\\", "/").rsplit("/", 2)[-2:])
    else:
        print("To convert online img path {}".format(img_abs_path))
        online_img_path = img_path_online2local(img_abs_path)

    token = q.upload_token(BUCKET_NAME, online_img_path, 3600)
    try:
        ret, info = put_file(token, online_img_path, img_abs_path)
    except FileNotFoundError as e:
        print("No this local file: {}".format(img_abs_path))
        return img_abs_path
    else:
        online_img_path = DOMAIN + "/" + online_img_path
        print("Uploaded to: " + online_img_path)
        return online_img_path


def md_imgs_convert2online(md_file_path: str, replace: bool):
    print("Open md content from {}".format(md_file_path))
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_str = f.read()
    print("Converting img hrefs in the md file...")
    md_str_converted = re.sub(r'!\[.*?\]\((.*?)\)', lambda x: get_online_img_path(x.group(1), md_file_path), md_str)

    if replace:
        md_file_path_new = md_file_path
    else:
        from datetime import datetime
        md_file_path_new = md_file_path.replace(".md", "_{}.md".format(int(datetime.now().timestamp())))
    with open(md_file_path_new, 'w', encoding="utf-8") as f:
        f.write(md_str_converted)
        print("Re-write md content to {}".format(md_file_path_new))

