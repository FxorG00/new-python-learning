# import math
# print(dir(math))
# dir 用于列出对象的属性和方法！
class MyClass:
    def __init__(self):
        self.x=1
        self.y=1
    def method1(self):
        pass
print(dir(MyClass())) # 实例对象
print(dir(MyClass)) # 类对象
