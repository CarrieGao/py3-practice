# _*_ coding: utf-8 _*_ 
import re

def trim1(s):
    # reg = r'^(\s*).*(\s*)$'
    # m = re.match(reg, s)
    # if m != None:
    #     m.groups()
    #     print(len(m.groups()))
    #     head = m.group(1)
    #     s = s[len(head):]
    # else:
    #     print ('can\'t not match reg')
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] != ' ':
        return trim1(s[1:])
    else:
        return trim1(s[:-1])

def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] != ' ':
        return trim(s[1:])
    else:
        return trim(s[:-1])


if __name__ == '__main__':
    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')