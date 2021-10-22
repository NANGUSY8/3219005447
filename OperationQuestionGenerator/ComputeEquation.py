from GenerateEquation import check_fraction
import fractions


def compute_equation(origin_equation):
    """
    处理式子并计算出式子的答案
    :param origin_equation: 随机式子
    :return:
    """
    try:
        equation = origin_equation.split(' ')  # 将式子去掉空格
        for i in range(len(equation)):
            elem_type = elem_type_judge(equation[i])  # 判断当前元素类型
            if elem_type == 'f':  # 元素为分数
                if '`' in equation[i]:  # 为带分数
                    integer, fraction = equation[i].split('`')  # 把带分数分割成整数和分数
                    # 将带分数转化为假分数
                    equation[i] = '({}+fractions.Fraction(\'{}\'))'.format(integer, fraction)
                else:  # 为真分数
                    equation[i] = 'fractions.Fraction(\'{}\')'.format(equation[i])
            elif elem_type == 'n':  # 元素为数值
                equation[i] = 'fractions.Fraction(\'{}\')'.format(equation[i])
            elif elem_type == 'o':  # 元素为运算符，÷、x 要改为/、*，+、-不变
                if equation[i] == '÷':
                    equation[i] = '/'
                    if equation[i + 1] == '(':  # 如果括号内结果为0即除数为0，返回异常
                        j = i + 1
                        formula = ''
                        while equation[j] != ')':   # 获取括号内的式子
                            formula += equation[j]
                            formula += ' '
                            j += 1
                        formula += equation[j]
                        # print(formula)
                        result_f = compute_equation(formula)
                        # print(result_f)
                        if result_f == '0':
                            return '除数为0'
                if equation[i] == 'x':
                    equation[i] = '*'
            elif elem_type == 'e':  # 元素为等号
                equation[i] = ''
        final_equation = ''.join(equation)  # 连接字符串，即为最终等式

        result = eval(final_equation)
        if result < 0:
            return '-1'
        else:
            return check_fraction(result)  # 检查结果，如果为假分数，化为带分数
    except ValueError:
        print('the equation is wrong')
        return '-1'


def elem_type_judge(elem):
    """
    判断元素类型
    :param elem: 元素
    :return: 返回代表其类型的字母
    """
    # print(elem)
    if type(elem) != str:
        raise TypeError
    if '/' in elem or '`' in elem:  # 出现分数即返回f
        return 'f'
    elif elem in ['+', '-', 'x', '÷']:
        return 'o'  # 出现四则运算符号则返回o
    elif elem == '=':
        return 'e'  # 出现等号则返回e
    elif elem.isdigit():
        return 'n'  # 若字符串只由数字组成即自然整数，则返回n
    elif elem == '(' or elem == ')':
        return 'b'
    else:
        raise ValueError
