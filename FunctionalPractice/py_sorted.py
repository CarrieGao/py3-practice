# _*_ coding: utf-8 _*_

def by_name(t):
    return t[0].lower()

def by_score(t):
    return t[1]


if __name__ == '__main__':
    print(sorted([36, 5, -12, 9, -21]))
    s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    print(s)
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    s2 = sorted(L, key = by_name)
    print(s2)
    s3 = sorted(L, key = by_score)
    print(s3)