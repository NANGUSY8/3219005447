# 判断重复方法
from BinaryTree import *


def is_repeat(express_set, expression):
    a = generate_suffix(expression)  # expression转化为后缀表达式
    a_tree = new_tree(a)  # 再生成二叉树
    for i in express_set:
        b_suffix = generate_suffix(i)  # expression_set的其中一个expression转化为后缀表达式
        b_binary_tree = new_tree(b_suffix)
        if same_judge(a_tree) == same_judge(b_binary_tree):  # 判断两个二叉树是否相同
            return True
    return False


# 将中缀表达式改成后缀表达式
def generate_suffix(expression):
    if not expression:
        return []
    operators = {   # 定义加减乘除的优先级
        '+': 1,
        '-': 1,
        'x': 2,
        '÷': 2,
    }
    suffix_stack = []  # 后缀表达式栈
    operators_stack = []  # 运算符栈
    exp_split = expression.split(' ')  # 去掉空格
    for i in exp_split:
        if i not in ['+', '-', 'x', '÷']:  # 非运算符
            if i == '(':  # 左括号直接入运算符栈
                operators_stack.append(i)
            elif i == ')':
                # 如果运算符栈不为空，那么直接出栈，添加到后缀表达式栈，直到遇到左括号
                while len(operators_stack) > 0:
                    op = operators_stack.pop()
                    if op == "(":
                        break
                    else:
                        suffix_stack.append(op)
            else:   # 操作数直接入后缀表达式栈
                suffix_stack.append(i)
        else:   # 运算符
            while len(operators_stack) >= 0:
                if len(operators_stack) == 0:
                    operators_stack.append(i)  # 空栈，直接压入
                    break
                else:
                    # 如果运算符栈不为空，则取出栈顶元素op
                    op = operators_stack.pop()
                    # 如果op是'('或者当前操作符算术优先级高于op,直接入栈
                    if op == '(' or operators[i] > operators[op]:
                        operators_stack.append(op)
                        operators_stack.append(i)
                        break
                    else:   # 否则运算符入后缀表达式栈
                        suffix_stack.append(op)

    while len(operators_stack) > 0:
        suffix_stack.append(operators_stack.pop())

    return suffix_stack
