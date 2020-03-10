from imgs_convert import run_conversion


if __name__ == '__main__':
    md_file_path = r"F:\MyProjects\PycharmProjects\NC_PyTorch\utils\eml\01_KNN\南川深度学习笔记01：KNN的精髓（附基于Cifar10的源码实现）.md"
    run_conversion(md_file_path, replace=False)

    print("ATTENTION! \n"
          "After the conversion, PLEASE use the converted .md file as your script and save as the raw .md file.")