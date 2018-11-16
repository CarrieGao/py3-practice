#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# function.py
import sys
import math

def quadratic(a, b, c):
    return (-b+ math.sqrt(b*b - 4*a*c))/(2*a),(-b - math.sqrt(b*b - 4*a*c))/(2*a)

def person(name, age,**kw): 
    print('name:', name, 'age:', age, 'other:', kw)

def personMethod2(name, age, *, city='Beijing', job):
    print(name, age, city, job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

if __name__ == '__main__':
    print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
    person('Michael', 30)
    person('Ann', 33, city='BeiJing')
    extra = {'city': 'BeiJing', 'job':'Engineer'}
    person('Bob', 24, **extra)
    personMethod2('Jack', 24, job='Engineer')

    f1(1, 2)
    f1(1, 2, c=3)
    f1(1, 2, 3, 'a', 'b')
    f1(1, 2, 3, 'a', 'b', x=99)
    f2(1, 2, d=99, ext=None)
    f2(1, 2, d=99, ext=None, y=3)
    # print (fact(981))
    print (fact2(1000))
