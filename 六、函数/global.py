# var1=20
# def func() :
#      var1=100 # 这是一个赋值操作，在函数体内部，所以会当成这是一个局部变量，创建一个新的局部变量
#     # var1+=10 这个也是一个赋值操作，也是当成局部变量，但是找不到定义
#     print(var1)
# func()
# print(var1)

list0=[1,2,3]
def func() :
    list0[0]=100 # 这是一个修改操作，所以不会默认当成局部变量
    print(list0)
func()
print(list0)