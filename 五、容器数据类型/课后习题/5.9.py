# 9）给定一个元组fruits = ("apple", "banana", "cherry", "date", "elderberry")，
# 编写一个程序，找出元组中最长的元素。
fruits = ("apple", "banana", "cherry", "fate", "elderberry")
# max 是字典序最大值
print(max(fruits))
pos=0
for i in range(0,len(fruits)):
    if len(fruits[i])>len(fruits[pos]):
        pos=i
print(fruits[pos])