class Person :
    """这是人的类""" # 类说明文档 doc
    home="earth" # 类属性，就是 Person 这个类自带的属性，因为类也是对象！
    def __init__(self,age):
        print("调用了 __init__ 方法！")
        self.age=age # 实例属性，就是小明、小红这些实例的年龄
    def say(self):
        print(f"hello my age is{self.age}")
xiaoming=Person(15) # 创建实例
xiaoming.say()
print(Person.home)