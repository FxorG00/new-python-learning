# 8）给定一个字符串str1 = "apple,banana,cherry,date"，
# 将该字符串按照,分隔，存储在一个列表中，并将列表中的元素首字母大写，
# 最后将修改后的列表元素用-连接成一个新的字符串。
str1 = "apple,banana,cherry,date"
# str.split(x) 按照 x 去分隔字符串，默认按空格分
list1=str1.split(',')
print(list1)
for i in range(0,len(list1)):
    # print(type(list1[i]))
    # str.capitalize(): 将字符串首字母大写，其他字母小写
    list1[i]=list1[i].capitalize()
print(list1)
# join 参加，联合
new_str='-'.join(list1)
print(new_str)