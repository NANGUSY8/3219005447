# 二叉树的结点
import operator


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
