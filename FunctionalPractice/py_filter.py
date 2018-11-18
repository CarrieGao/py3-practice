# _*_ coding:utf-8 _*_

def is_odd(n):
    return n%2 == 1

def not_empty(s):
    return s and s.strip()

def _odd_iter():
    '''
    这是一个生成器，并且是一个无限序列。
    '''
    n= 1
    while True:
        n = n+1
        yield n


def _not_divisible(n):
    return lambda x: x%n >0


def primes():
    '''
        计算素数的一个方法是埃氏筛法,取一个自然数系列的第一个数，这一定是一个素数，然后整个系列得到一个新系列，重复上一步
    '''
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it= filter(_not_divisible(n), it)

def is_palindrome(n):
    if n <= 0:
        return False
    sn = str(n)
    l = len(sn)
    while True:
        if l > 1:
            if sn[0] == sn[l-1]:
                sn = sn[1:][-1:]
                l = len(sn)
            else:
                return False
        else:
            break

    return True



if __name__ == '__main__':
    # 打印1000以内的素数:
    # count = 0
    # for n in primes():
    #     if n < 1000:
    #         print(n)
    #         count = count +1
    #     else:
    #         break
    # print('total count is %d'%count)

    # 测试:
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')