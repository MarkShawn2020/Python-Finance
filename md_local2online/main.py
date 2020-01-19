from imgs_convert import run_conversion


if __name__ == '__main__':
    md_file_path = r"C:\Users\WZ988KR\PycharmProjects\Daily-Python-Learning\NC_P.F.A\CH01 - The Very Intro to Python.md"
    run_conversion(md_file_path, replace=False)

    print("ATTENTION! \n "
          "After the conversion, PLEASE use the converted .md file as your script and save as the raw .md file.")