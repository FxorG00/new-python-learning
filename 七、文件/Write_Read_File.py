"""# 打开文件，获取 file 对象
f=open("test.txt","w")
# 写入数据
f.write("hello\n")
f.write("I'm back\n")
# 关闭文件
f.close()"""
file=open("test.txt","r")

"""
print(file.read()) # 读入所有
print(file.read(3)) # 读 3 个字节

print(file.readline(),end="") # 读一行数据，换行也读了
print(file.readline(),end="")
"""
# print(file.readlines()) # 读取所有行，搞成个列表
print(type(file.read()))

file.close()