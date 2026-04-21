class Father1:
    def __init__(self,val1,**kwargs):
        # kwargs 是一个字典，那你传参的时候肯定是
        # val1=val1,val2=val2 而不是传一个 {"val1",val1} 这样的字典
        # 所以需要解包
        self.val1=val1
        super().__init__(**kwargs)
class Father2:
    def __init__(self,val2,**kwargs):
        self.val2=val2
        super().__init__(**kwargs)
class Son(Father1,Father2) :
    def __init__(self,val1,val2): # 相当于对 init 方法进行重写
        # 直接写
        # self.val1=val1
        # self.val2=val2

        # 直接调用父类命名空间的 init 方法
        # Father1.__init__(self,val1)
        # Father2.__init__(self,val2)

        # 利用 super() 实际上是在 mro 中找上一个的性质
        super().__init__(val1=val1,val2=val2)
p1=Son(15,20)
print(Son.__mro__)
print(p1.val1,p1.val2)