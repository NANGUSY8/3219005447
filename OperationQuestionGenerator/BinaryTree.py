import operator


# 二叉树的结点
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 生成二叉树
def new_tree(exp):
    tree_stack = []
    for i in exp:
        parent = Node(i)
        if i not in ['+', '-', 'x', '÷']:
            # 操作数
            tree_stack.append(parent)
        else:
            # 操作符
            right = tree_stack.pop()
            left = tree_stack.pop()
            parent.right = right
            parent.left = left
            tree_stack.append(parent)

    parent = tree_stack[-1]
    return parent


# 判断二叉树是否相同
def same_judge(root):
    if not root.left:
        if not root.right:
            return root.value
    elif root.value == '+' or root.value == 'x':
        left = same_judge(root.left)
        right = same_judge(root.right)
        if operator.le(left, right):
            return root.value + left + right
        else:
            return root.value + right + left
    else:
        return root.value + same_judge(root.left) + same_judge(root.right)


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
