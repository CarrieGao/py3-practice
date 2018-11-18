# _*_ coding: utf-8 _*_


if __name__ == '__main__':
    print(__name__)

    # List Comprehensions
    # Python's conditional expression is a if C else b and can't be used as:
    # 
    # [a for i in items if C else b]
    # The right form is:
    # 
    # [a if C else b for i in items]
    # Even though there is a valid form:
    # 
    # [a for i in items if C]
    # But that isn't the same as that is how you filter by C, but they can be combined:
    # 
    # [a if tC else b for i in items if fC]

    # example
    l = [22, 13, 45, 50, 98, 69, 43, 44, 1]
    #  SyntaxError: invalid syntax
    # l2 = [x+1 for x in l if x >= 45 else x+5]
    # print(l2)
    l2 = [x+1 if x >= 45 else x+5 for x in l]
    print(l2)
    l3 = [[x+5,x+1][x >= 45] for x in l]
    print (l3)
    
    l4 = [x+1 if x >= 45 else x+5 for x in l if x< 20]
    print(l4)

    # theory of list Comprehensions???
    # Like in [a if condition1 else b for i in list1 if condition2], the two ifs with condition1 and condition2 doing two different things. The part (a if condition1 else b) is from a lambda expression:
    # 
    # lambda x: a if condition1 else b
    # while the other condition2 is another lambda:
    # 
    # lambda x: condition2
    # Whole list comprehension can be regard as combination of map and filter:
    # 
    # map(lambda x: a if condition1 else b, filter(lambda x: condition2, list1))
    # practice 
    L1 = ['Hello', 'World', 18, 'Apple', None]
    L2 = [s.lower() for s in L1 if isinstance(s, str) == True ]
    print(L2)
    if L2 == ['hello', 'world', 'apple']:
       print('测试通过!')
    else:
       print('测试失败!')