from .general import *


def upload_img_to_cloud(doc_md: str, cookie_str: str) -> str:
    """

    :param doc_md:
    :return:
    """
    pass
    return doc_md


def download_attached_file(attach_href, attach_name, doc_dir, cookie_str: str):
    """

    :param doc_href:
    :param doc_name:
    :param doc_dir:
    :return:
    """
    file_path = os.path.join(doc_dir, attach_name)
    if os.path.exists(file_path):
        return print("【{}】 existed @ {}.".format(attach_name, doc_dir))

    from contextlib import closing

    with closing(requests.get(attach_href, stream=True, headers={"Cookie": cookie_str})) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        progress = ProgressBar(attach_name, total=content_size,
                               unit="KB", chunk_size=chunk_size, run_status="正在下载", fin_status="下载完成")

        with open(file_path, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                progress.refresh(count=len(data))


def get_doc_title(driver):
    doc_title_ele = wait_element(driver, EC.element_to_be_clickable((By.CSS_SELECTOR, ".notetitle-ctn h2")))
    return doc_title_ele.text


def auto_scroll_doc_list(driver):
    """
    在笔记列表页从头滚到尾，以一次性加载所有文章
    ！ 但是，如果滑条已经到了中间的某些位置，则重新调用该函数会报错
    由于selenium的滚动有多种实现方式，本种方式只能保证程序正常运行时是可行的
    :param driver:
    :return:
    """

    def _get_final_note_ele(driver):
        return driver.find_elements_by_class_name("note-list-item")[-1]

    def _get_total_notes_cnt(driver):
        return len(driver.find_elements_by_class_name("note-list-item"))

    import time
    cur_final_note_ele = None
    while True:
        now_final_note_ele = _get_final_note_ele(driver)
        now_final_note_ele.click()
        time.sleep(3)
        if cur_final_note_ele == now_final_note_ele:
            break
        else:
            cur_final_note_ele = now_final_note_ele

    print("Total doc count: {}".format(_get_total_notes_cnt(driver)))


def save_doc_md(driver, doc_path:  str, cookie_str: str):
    def switch_mode(mode: str):
        print("Switching to {} mode...".format(mode.upper()))
        btn_ele = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "{}-btn".format(mode))))
        btn_ele.click()

    switch_mode("edit")
    driver.switch_to.frame(driver.find_element_by_class_name("wiz-editor-iframe"))

    # 获取.md格式的文章内容，需要停留一下比较好
    time.sleep(2)
    # 有些是表格，有些是md，md的话可以直接用webElement.text方式获取内容，但是表格等需要用innerHTML或者outerHTML方式
    # 本处采用innerHTML
    doc_md = driver.find_element_by_tag_name("body").get_attribute("innerHTML")

    if MD_IMGS_TO_UPLOAD:
        doc_md = upload_img_to_cloud(doc_md, cookie_str)

    driver.switch_to.default_content()
    switch_mode("backtoread")

    if not os.path.exists(doc_path):
        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(doc_md)



def save_doc_attached_files(driver: webdriver.Firefox, doc_dir: str, cookie_str: str):
    attach_ul = driver.find_element_by_id("attach-ul")
    if attach_ul:
        for attach_li in attach_ul.find_elements_by_tag_name("li"):
            attach_name = attach_li.get_attribute("data-attachname")
            attach_href = attach_li.find_element_by_tag_name("a").get_attribute("href")
            download_attached_file(attach_href, attach_name, doc_dir, cookie_str)


def doc_guid2href(doc_guid: str, current_url: str):
    return re.sub("(?<=dc=).*?(?=&)", doc_guid, current_url)


def parse_doc(driver: webdriver.Firefox, doc_href: str):
    driver.get(doc_href)
    group_ele = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kbGroupName"))
    )

    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    group_dir = os.path.join(DATA_DIR, group_ele.text)
    if not os.path.exists(group_dir):
        os.mkdir(group_dir)

    doc_title = get_doc_title(driver)

    doc_dir = os.path.join(group_dir, doc_title.rsplit(".", 1)[0])
    if not os.path.exists(doc_dir):
        os.mkdir(doc_dir)

    doc_path = os.path.join(doc_dir, doc_title)
    cookie_str = cookie_jar2str(driver.get_cookies())

    save_doc_md(driver, doc_path, cookie_str)

    if ATTACHED_FILES_TO_DOWNLOAD:
        save_doc_attached_files(driver, doc_dir, cookie_str)

    print("Saved files at: {}\n".format(doc_dir))


def driver_parse(driver: webdriver.Firefox, wiz_page: str):
    driver.get(wiz_page)
    time.sleep(5)
    doc_href_list = [doc_guid2href(doc_li.get_attribute("data-docguid"), driver.current_url)
                     for doc_li in driver.find_elements_by_css_selector("#doclist-ctn li")]
    for doc_href in doc_href_list:
        parse_doc(driver, doc_href)

    print("Finished parsing wiz_page: {}\n".format(wiz_page))

    """
    # 以下形式是不行的， 因为Selenium挑战其他链接后，元素会发生变化
    # 所以只能一次性获得所有的静态链接，然后依次跳转访问
    for doc_li in driver.find_elements_by_css_selector("#doclist-ctn li"):
    doc_guid = doc_li.get_attribute("data-docguid")
    doc_href = doc_guid2href(doc_guid, driver.current_url)
    parse_doc(driver, doc_href)
    """

