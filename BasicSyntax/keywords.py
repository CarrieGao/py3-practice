#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# keywords.py
import sys
import keyword


if __name__ == '__main__':
    print(sys.builtin_module_names)
    print("Python version: ", sys.version_info)
    print("Python keywords: ", keyword.kwlist)
    
    name = input('please enter your name: ')
    print('hello,', name)
