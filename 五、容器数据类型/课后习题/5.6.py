# 6）给定一个字符串sentence = "Hello, World!"，
# 编写一个程序，将字符串中的所有小写字母转换为大写字母，并输出结果。
sentence = "Hello, World!"
# str.upper(): 将所有字符转为大写
# =sentence.upper()
# print(s1)
# 字符串是不可变的、有序的。
# 字符串中元素不可修改。 不能用 s[i] 去修改字符串元素
# 但是 s1 作为一个变量，是可以整体修改的，就是可以 s1="abcde"
# 方法返回新字符串，拿变量去接收而已
s2=""
for i in range(0,len(sentence)):
    if sentence[i].islower():
        s2+=sentence[i].upper()
    else:
        s2+=(sentence[i])
# s2=s2.upper()
print(s2)