# _*_ coding:utf-8 _*_

def count1():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count():
    fs = []
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

def createCounter():
    i = 0
    def counter():
        nonlocal i 
        i= i + 1
        return i
    return counter

    
if __name__ == '__main__':

    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())

    # 测试:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')

    # 匿名函数 lambda
    L = list(filter(lambda x: x%2 == 1, range(1, 20)))
    print(L)