import sys

from BinaryTree import *
from ComputeEquation import compute_equation
from GenerateEquation import generate_equation
from Proofread import proofreading


# main函数
def main():
    try:
        # sys.argv[1:5]只读取前四个输入字符   parameter1/parameter2为两个参数
        parameter1, value1, parameter2, value2 = sys.argv[1:5]
        choice = choice_fun(parameter1, parameter2)
        if choice == 1:  # 为生成题目和答案的过程
            n = value1
            r = value2
            generate_equation(r)
            generate_file(n, r)
            print("生成题目成功！请查看 'Exercises.txt' 和 'Answers.txt'\n")
        elif choice == 2:  # 为校对给定题目和答案的过程
            e = value1
            a = value2
            proofreading(e, a)
            print("校对完成！请在 'Grade.txt' 查看结果\n")
    except IOError:
        print("Error:输入参数错误,请检查后重新输入")


def generate_file(q_num, num_range):
    """
    # 根据个数和范围生成随机式子，并把式子和结果装进txt文件
    :param q_num: 生成题目的个数
    :param num_range: 数的范围
    :return:
    """
    q_num = int(q_num)
    num_range = int(num_range)
    q_list = list()
    a_list = list()
    count = 0
    while count < q_num:  # 小于式子指定数量时
        # 判断重复，0为不重复，1为重复
        repeat = 0
        equation = generate_equation(num_range)  # 生成随机式子
        answer = compute_equation(equation)  # 计算式子的答案

        a = generate_suffix(equation)  # equation 转化为后缀表达式
        a_tree = new_tree(a)  # 生成二叉树
        tree_list = list()

        while len(tree_list) > 0:
            for x in tree_list:
                if same_judge(a_tree) == same_judge(x):  # 判断两个二叉树是否相同
                    repeat = 1

        # repeat = is_repeat(q_list, equation)  # 判断式子是否重复
        if answer == '除数为0':
            continue
        elif answer != '-1' and repeat == 0:  # 答案不出错以及不重复
            # 将式子和答案写入列表中
            q_list.append(equation)
            a_list.append(answer)
            count += 1
            tree_list.append(a_tree)
    for list_content, path in zip([q_list, a_list], ['Exercises.txt', 'Answers.txt']):
        order_num = 1
        with open(path, 'w') as f:
            for line in list_content:  # 将列表中的内容写入文件
                content = str(order_num) + ".  " + line
                f.write(content)
                f.write('\n')
                order_num += 1
            # print(order_num)
            # f.close()


def choice_fun(s1, s2):
    """
    # 根据参数选择过程，参数错误抛出异常
    :param s1:
    :param s2:
    :return:
    """
    # 当输入-n xx -r xx 时，即是生成题目和答案的过程
    if s1 == '-n' and s2 == '-r':
        return 1
    # 当输入-e xx -a xx 时，即是校对给定题目和答案的过程
    elif s1 == '-e' and s2 == '-a':
        return 2
    else:
        ex = Exception('Error:参数格式错误！')
        raise ex


if __name__ == '__main__':
    # main()

    generate_equation(10)
    generate_file(1, 10)
