# _*_ coding: utf-8 _*_
from functools import reduce
import operator
from collections import Iterable

def f(x):
    return x*x

def add(x, y):
    return x+y

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    return reduce(fn, map(char2num, s))


def str2float(s):
    def fnInt(x, y):
        return x*10 + y
    def fnDec(x, y):
        return x*0.1 +y
    strs =  s.split('.')
    res = 0
    if len(strs) > 1:
        integer = reduce(fnInt, map(char2num, strs[0]))
        decimals = reduce(fnDec, map(char2num, strs[1][ : :-1]))*0.1
        res = integer + decimals
    elif len(strs) > 0:
        res = reduce(fnInt, map(char2num, strs[0]))
    return res


# define by MichaelLiao
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2floatL(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

def normalize(name):
    s = ''
    for index, letter in enumerate(name):
        if index == 0:
            s = s+letter.upper()
        else:
            s = s+letter.lower()
    return s

def prod(L):
    if isinstance(L, Iterable) == True:
        return reduce(lambda x, y: x*y, L)

if __name__ == '__main__':
    r = map(f, list(range(1, 9)))
    print(list(r))
    re = reduce(add, list(range(1, 9)))
    print(re)
    ret = map(operator.add, range(1, 5), range(2,6))
    print(list(ret))
    ret = map(operator.lt, range(1, 5), range(2,6))
    print(list(ret))


    # 测试:
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(normalize, L1))
    print(L2)

    # test
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
    if prod([3, 5, 7, 9]) == 945:
        print('测试成功!')
    else:
        print('测试失败!')

    # test
    print('str2float(\'123.456\') =', str2float('123.456'))
    if abs(str2float('123.456') - 123.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
    if abs(str2float('123') - 123) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
    if abs(str2float('0.456') - 0.456) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
    print(str2float('0'))
    print(str2float('123.456'))
    print(str2float('123.45600'))
    print(str2float('0.1234'))
    #print(str2float('.1234'))
    print(str2float('120.0034'))

    # ------------------------------------------------------------------------------------------
    ## python中global 和 nonlocal 的作用域
    #python引用变量的顺序： 当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量 。
    #nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
    def scope_test():
        def do_local():
            spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
        def do_nonlocal():
            nonlocal  spam        #使用外层的spam变量
            spam = "nonlocal spam"
        def do_global():
            global spam
            spam = "global spam"
        spam = "test spam"
        do_local()
        print("After local assignmane:", spam)
        do_nonlocal()
        print("After nonlocal assignment:",spam)
        do_global()
        print("After global assignment:",spam)
    # test global and nonlocal
    scope_test()
    print("In global scope:",spam)