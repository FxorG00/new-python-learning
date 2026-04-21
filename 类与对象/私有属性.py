# class Person:
#     # 加 __ 就可以私有化属性/方法
#     # 相当于底层把 __名字 改写成了 _类名__名字
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age # 把 age 私有化了！
#     def get_age(self):
#         if self.__age>18: # 进行一个拦截
#             return 18
#         return self.__age
#     def set_age(self,age):
#         self.__age=age
# p1=Person("小明",60)
# print(p1.get_age()) # 永远 18 岁
# # 这个就是封装，把 __age 私有化，只暴露 set 跟 get 方法

class Person:
    # 加 __ 就可以私有化属性/方法
    # 相当于底层把 __名字 改写成了 _类名__名字
    def __init__(self,name,age):
        self.name=name
        self.__age=age # 把 age 私有化了！
    @property
    def age(self):
        if self.__age>18: # 进行一个拦截
            return 18
        return self.__age
    @age.setter
    def age(self,age):
        self.__age=age
p1=Person("小明",60)
print(p1.age)
p1.age=15
print(p1.age)