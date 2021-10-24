from ComputeEquation import compute_equation


def proofreading(qf, af):
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
    with open('Grade.txt', 'w') as f:
        f.write(file_str)
    print('校对成功！可在Grade.txt中查看结果:\n')
