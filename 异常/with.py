try:
    with open("qwq.txt","w") as f:
        f.write(a)
    # 会自动调 f.close()
except:
    print("出现异常！")
finally:
    print(f"文件关闭状态{f.closed}")
print("end")