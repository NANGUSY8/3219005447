from main import *
import unittest

qlist = ['Exercises1.txt', 'Exercises2.txt', 'Exercises3.txt', 'Exercises4.txt', 'Exercises5.txt',
         'Exercises6.txt', 'Exercises7.txt', 'Exercises8.txt',
         'Exercises9.txt', 'Exercises10.txt', ]
alist = ['Answers1.txt', 'Answers2.txt', 'Answers3.txt', 'Answers4.txt', 'Answers5.txt',
         'Answers6.txt', 'Answers7.txt', 'Answers8.txt', 'Answers9.txt', 'Answers10.txt']
glist = ['Grade1.txt', 'Grade2.txt', 'Grade3.txt', 'Grade4.txt', 'Grade5.txt', 'Grade6.txt', 'Grade7.txt'
    , 'Grade8.txt', 'Grade9.txt', 'Grade10.txt']


def proofreadingtest(qf, af, gf):
    """
    校对答案是否正确，并将校对结果放入Grade.txt
    :param qf: 题目文件路径
    :param af: 答案文件路径
    :return:
    """

    q_list, a_list = [list(), list()]
    # zip() 打包为元组的列表[(q_list,qf),(a_list,af)]
    for list_content, path in zip([q_list, a_list], [qf, af]):
        try:
            # 打开文件，将文件中的每行内容添加到列表中
            with open(path) as f:
                for line in f.readlines():
                    list_content.append(line.strip())
        except FileNotFoundError:
            print('文件不存在或路径错误')

    min_len = min(len(q_list), len(a_list))
    proof = {'Correct': list(), 'Wrong': list()}
    # 计算每道题目的答案是否与答案文件中的相等
    for i in range(min_len):
        equ_list = q_list[i].split('.')
        ans_list = a_list[i].split('.')
        print(equ_list[1])
        # 相等在Correct列表中添加序号
        if compute_equation(equ_list[1]) == ans_list[1]:
            proof['Correct'].append(i + 1)
        else:
            # 不等在Wrong列表中添加序号
            proof['Wrong'].append(i + 1)
    file_str = 'Correct:{}{}\nWrong:{}{}'.format(
        len(proof['Correct']), str(proof['Correct']),
        len(proof['Wrong']), str(proof['Wrong']))
    # 'w' 代表文件为只写模式
    with open(gf, 'w') as f:
        f.write(file_str)
    print('校对成功！可在Grade.txt中查看结果:\n')


def generate_filetest(q_num, num_range, qf, af):
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
    tree_list = list()
    count = 0
    while count < q_num:  # 小于式子指定数量时
        # 判断重复，0为不重复，1为重复
        repeat = 0
        equation = generate_equation(num_range)  # 生成随机式子
        answer = compute_equation(equation)  # 计算式子的答案

        a = generate_suffix(equation)  # equation 转化为后缀表达式
        a_tree = new_tree(a)  # 生成二叉树
        '''
        if len(tree_list) == 0:
            tree_list.append(a_tree)
        else:
            for x in a_list:
                if answer == x:  # 两个式子的答案相同时
                    for y in tree_list:
                        if same_judge(a_tree) == same_judge(y):  # 判断两个二叉树是否相同
                            repeat = 1
        '''
        # repeat = is_repeat(q_list, equation)  # 判断式子是否重复
        if answer == '除数为0':
            continue
        elif answer != '-1' and repeat == 0:  # 答案不出错以及不重复
            # 将式子和答案写入列表中
            q_list.append(equation)
            a_list.append(answer)
            count += 1
            tree_list.append(a_tree)
    for list_content, path in zip([q_list, a_list], [qf, af]):
        order_num = 1
        with open(path, 'w') as f:
            for line in list_content:  # 将列表中的内容写入文件
                content = str(order_num) + "." + line
                f.write(content)
                f.write('\n')
                order_num += 1


def test_case10():
    generate_equation('10')
    generate_filetest('10000', '10', qlist[9], alist[9])
    proofreadingtest(qlist[9], alist[9], glist[9])


class mytest(unittest.TestCase):
    def test_case1(self):
        generate_equation('10')
        generate_filetest('10', '10', qlist[0], alist[0])
        proofreadingtest(qlist[0], alist[0], glist[0])

    def test_case2(self):
        generate_equation('10')
        generate_filetest('100', '10', qlist[1], alist[1])
        proofreadingtest(qlist[1], alist[1], glist[1])

    def test_case3(self):
        generate_equation('10')
        generate_filetest('220', '10', qlist[2], alist[2])
        proofreadingtest(qlist[2], alist[2], glist[2])

    def test_case4(self):
        generate_equation('10')
        generate_filetest('520', '10', qlist[3], alist[3])
        proofreadingtest(qlist[3], alist[3], glist[3])

    def test_case5(self):
        generate_equation('10')
        generate_filetest('1000', '10', qlist[4], alist[4])
        proofreadingtest(qlist[4], alist[4], glist[4])

    def test_case6(self):
        generate_equation('10')
        generate_filetest('2000', '10', qlist[5], alist[5])
        proofreadingtest(qlist[5], alist[5], glist[5])

    def test_case7(self):
        generate_equation('10')
        generate_filetest('2200', '10', qlist[6], alist[6])
        proofreadingtest(qlist[6], alist[6], glist[6])

    def test_case8(self):
        generate_equation('10')
        generate_filetest('4396', '10', qlist[7], alist[7])
        proofreadingtest(qlist[7], alist[7], glist[7])

    def test_case9(self):
        generate_equation('10')
        generate_filetest('6300', '10', qlist[8], alist[8])
        proofreadingtest(qlist[8], alist[8], glist[8])


if __name__ == '__main__':
    unittest.main
