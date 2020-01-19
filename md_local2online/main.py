from md_local2online import md_imgs_convert2online


if __name__ == '__main__':
    md_file_path = r"C:\Users\WZ988KR\PycharmProjects\Daily-Python-Learning\NC_P.F.A\CH01_TheVeryIntroductionToPython\CH01_TheVeryIntroToPython.md"
    md_imgs_convert2online(md_file_path, replace=False, img_dir_path="CH01_TheVeryIntroToPython.assets")