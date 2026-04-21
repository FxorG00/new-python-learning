try:
    result = 3 / 0
    print("发生异常了")
except ZeroDivisionError as e:
    print(e)
except (RuntimeError, TypeError, NameError) as e:
    print(e)
except:
    # 出现了异常，并且没有被上面的 except 捕获到，那么就进入到这里！是我没有预想到的异常！
    print("Unexpected error")
print("End")