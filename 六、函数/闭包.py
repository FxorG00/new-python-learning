"""
    闭包的需求：在一个函数里面访问另一个函数中定义的变量
"""

def outer() :
    a=10
    inner(a)
def inner(a) :
    print(a)
outer()