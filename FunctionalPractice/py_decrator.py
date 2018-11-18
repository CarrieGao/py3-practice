# _*_ coding _*_:
import functools
import time

def log0(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    wrapper.__name__ = func.__name__
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'% (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        before = time.time()
        print('metric call  %s():'%func.__name__)
        res = func(*args, **kw)
        after = time.time()
        print('%s executed in %s ms' % (func.__name__, after-before))
        return res
    return wrapper



@log0
def now0():
    print('today 2018/11/18')

@log('execute')
def now():
    print('today 2018/11/18 PM 15:07')

if __name__ == '__main__':
    # now0()
    # print(now0.__name__)

    # now()
    # print(now.__name__)

    # 测试
    @metric
    def fast(x, y):
        time.sleep(0.0012)
        return x + y

    @metric
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z

    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')