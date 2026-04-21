class Person:
    home="earth"
    def method1(self,msg):
        print("method1!"+msg)
    @classmethod
    def class_method(cls):
        print(cls.home)
    @staticmethod
    def static_method():
        print("this is a static method")
Person.class_method() # 类方法
p1=Person()
p1.method1("hahaha") # 实例方法
p1.static_method() # 静态方法，只依赖参数，不访问类和实例对象的属性
