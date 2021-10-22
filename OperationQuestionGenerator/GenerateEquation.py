import numpy as np
import fractions
import decimal


# 生成随机式子
def generate_equation(max_value):
    """
    :param max_value: 生成数的最大值
    :return: 生成的随机式子
    """
    operator = [' + ', ' - ', ' x ', ' ÷ ']  # 运算符前后加空格
    end_opt = ' ='
    # 随机生成自然数和分数的个数，但控制总和不超过4，从而控制题目不超过三个运算符
    num_nature, num_fraction = np.random.randint(1, 3, size=2)
    # 生成 [1,max_value) 之间的自然整数
    gen_nature = [str(x) for x in np.random.randint(1, max_value, size=num_nature)]

    # np.random.rand()产生的是[0,1)之间的小数，产生 num_fraction 个数
    # round()根据四舍五入来取值，+0.5是为了防止取值后为0
    gen_float = [str(round(x + 0.5, 1)) for x in np.random.rand(num_fraction)]
    gen_fraction = list()

    # decimal.Decimal()把 gen_float 中字符串类型转化为十进制数据，然后用fractions.Fraction()再次转化为分数
    for fraction in [fractions.Fraction(decimal.Decimal(x)) for x in gen_float]:
        # 通过 check_fraction 函数来检查分数，将结果添加至gen_fraction
        gen_fraction.append(check_fraction(fraction))

    equation = ''
    bag = gen_nature + gen_fraction  # 将生成的自然整数和分数存在bag里
    len_bag = len(bag)
    # left_bracket 生成左括号的位置,0代表不生成,1代表生成
    left_bracket = np.random.randint(0, 2)
    right_bracket = 0
    if left_bracket == 0:
        right_bracket = 0
    else:
        if len_bag == 3:
            left_bracket = np.random.randint(0, 3)
        elif len_bag == 4:
            left_bracket = np.random.randint(0, 4)
        # 生成有括号的位置
        if left_bracket > 0:
            if left_bracket != len_bag - 1:
                right_bracket = np.random.randint(left_bracket+1, len_bag)
            else:
                right_bracket = len_bag
    for i in range(len_bag):
        if left_bracket == i + 1:  # 加入左括号
            equation += '( '

        # 随机生成一个[0,len(bag))之间的整数
        randint = np.random.randint(len(bag))
        # 从 bag 取出第 randint 位的数，存进 equation 中
        equation += bag[randint]
        if i + 1 == right_bracket:  # 加入右括号
            equation += ' )'
        if i < len_bag - 1:
            # len_bag-1即是i的最大取值，所以当i<len_bag-1时，后面加随机操作符
            equation += operator[randint]
        else:
            # 当i=len_bag时，把等号补上，式子完成，跳出循环
            equation += end_opt
        bag.pop(randint)  # 当数取出的时候，应该把它从bag里去除
    return equation


# 检查分数形式，真分数不用改变，假分数变为真分数
def check_fraction(fraction):
    """
    :param fraction: 原分数
    :return: 返回处理后的分数
    """

    if fraction.numerator > fraction.denominator:  # 分子大于分母，即假分数
        rounding = fraction.numerator // fraction.denominator  # 提取带分数前面的整数
        if fraction - rounding == 0:  # 为整数
            fraction_str = '{}'.format(rounding)
        else:  # 不为整数
            fraction_str = '{}`{}'.format(rounding, fraction - rounding)
    else:  # 为真分数
        fraction_str = str(fraction)
    return fraction_str
