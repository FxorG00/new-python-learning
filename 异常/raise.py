# raise TypeError("哈哈哈") # 你直接抛出来，没人捕获你啊！抛给控制台了
def add(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x+y
    else:
        raise TypeError("你传进来的参数不全是整数！打回")
        # 抛出一个异常，那我下面可以来捕获了！
try:
    res=add(1,2.0)
except TypeError as e:
    print(e)
else:
    print(res)
    # 你只有函数跟类会隔离作用域，其他的是不会的，所以这里还是可以访问到 res
