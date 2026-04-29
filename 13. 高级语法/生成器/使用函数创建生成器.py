def fibo():
    a,b=0,1
    print("进来了！")
    while True:
        print("一次循环开始了！")
        yield b
        a,b=b,a+b
        print("一次循环结束了！")
f=fibo() # 没有执行这个 fibo() 函数
print(f)
# 第一次调用 next 的时候，才会去执行这个函数
print(next(f))
print("~~~~~~~~~~~~~~~~~")
print(next(f))
print("~~~~~~~~~~~~~~~~~")
print(next(f))