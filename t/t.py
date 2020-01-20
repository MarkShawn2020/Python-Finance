# -*-           coding: utf-8               -*- 
# ---------------------------------------------
# @Project:     Daily-Python-Learning
# @File:        t.py
# @Date:        2020/1/19
# @IDE:         PyCharm
# @Author:      Mark Shawn
# @Email:       shawninjuly@gmail.com
# ---------------------------------------------


# 以下是三个测试用例，这块代码补完之后要能直接运行。
def get_next_input_pos(cur_pos, TAB_WIDTH):
    """
    用三个双引号写在函数下面，表示注释，而且这里的注释是对于整个函数的说明，并且非常重要，因为当你进阶后可能会涉及到编写程序文档，而这里的说明可以自动变成文档的一部分。
    在这一组三引号内你可以输入任何正常文字，我在下面给一个比较标准的注释，供大家参考。
    -----------------------------------------------------------
    得到输入一个TAB键后，光标所在的输入位置
    :param cur_pos: 	输入时，当前已经输入的英文字符数，由于中文字符是按2-3个计的，因此此处只考虑英文
    :param TAB_WIDTH: 	每个TAB表示的固有的宽度，一般为4
    :return: int		应该返回一个整数值
    """

    if cur_pos % TAB_WIDTH == 0:
        # 当前正好处于位宽的结尾处，则下一个TAB键后，光标应该跳到下下个单元的开头
        print("Next pos will be: ", cur_pos + TAB_WIDTH + 1)

    else:
        # 否则，下个TAB键后，光标应该跳到下个单元的开头
        print(cur_pos)  # 这里留给大家自己思考，给我答案

# 以下是三个测试用例，这块代码补完之后要能直接运行。
get_next_input_pos(4, 4)
get_next_input_pos(9, 4)
get_next_input_pos(5, 2)