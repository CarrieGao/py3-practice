# _*_ coding: utf-8 _*_
from collections import Iterable, Iterator

def findMinAndMax(L):
    min = None
    max = None
    if isinstance(L, Iterable) == False:
        print('not a iterable')
        return (None, None)
    if len(L) == 0:
        return (None, None)
    for item in L:
        if  min == None or item <= min:
            min = item
        if  max == None or item >= max:
            max = item
    return (min, max)

if __name__ == '__main__':
    print(__name__)
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
    # Iterable 可作用于for循环,Python 6种类型的Iterable, list, dist, str, tuple, set, Iterator
    # Iterator 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
    # Python的Iterator对象表示的是一个数据流, 甚至可以表示一个无限大的数据流，例如全体自然数。表示一个惰性计算的序列；
    # list、dict、str虽然是Iterable，却不是Iterator,不过可以通过iter()函数获得一个Iterator对象。
    print(isinstance([], Iterator))
    print(isinstance({}, Iterator))
    print(isinstance((), Iterator))
    print(isinstance('abc', Iterator))
    print(isinstance('abc', Iterable))
    print(isinstance((x for x in range(10)), Iterator))
    print(isinstance((x for x in range(10)), Iterable))

    #
    # 首先获得Iterator对象:
    it = iter([1, 2, 3, 4, 5])
    # 循环:
    while True:
        try:
            # 获得下一个值:
            x = next(it)
            print('it %d'%x)
        except StopIteration:
            # 遇到StopIteration就退出循环
            print('遇到StopIteration就退出循环')
            break