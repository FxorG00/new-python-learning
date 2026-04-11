# 5）给定一个列表strings = ["hello", "world", "python", "is", "fun"]，
# 编写一个程序，将列表中的元素拼接成一个字符串，元素之间用空格分隔。
strings = ["hello", "world", "python", "is", "fun"]
new_str=""
for x in strings:
    new_str+=x+' '
print(len(new_str))

# x.join(seq) 以 x 为分隔符，将序列中所有的字符串合并成一个新的字符串
str2=' '.join(strings)
print(len(str2))