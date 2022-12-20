#!/usr/bin/python3
"""функция список строк --> список байт """

def inbytes(a):
    a= [i.encode('utf-8') for i in a]
    return a
res = inbytes(["Саша","Петя","Вася"])
print(f'{res}')

def instrings(b):
    b = [i.decode('utf-8') for i in b]
    return b
print(f'{instrings(res)}')
