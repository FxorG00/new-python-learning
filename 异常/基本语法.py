try:
    # 执行 try 的代码，如果有异常了，立马跳转到 except
    print("我开始 try！！！")
    res=10/0 # 这里出现异常后，try 的代码块就不会执行了！直接去 except
    print(f"执行完毕，没有出现异常，答案为 {res}")
except:
    print("出现异常了!")
print("程序执行完毕！")