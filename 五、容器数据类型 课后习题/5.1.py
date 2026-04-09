# 1）给定一个列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，
# 编写一个程序，将列表中所有的偶数元素删除

numbers=[1,2,3,4,5,6,7,8,9,10]
# 用 del 删，从后往前保证下标不会出错
# for i in range(len(numbers)-1,-1,-1) :
#     if numbers[i]%2==0 :
#         del numbers[i]
# for x in numbers :
#     print(x)

# 列表推导式：会生成一个新的列表
# numbers=[x for x in numbers if x%2!=0]
# print(numbers)

# list.remove(x): 删除第一次出现的 x
# 利用切片搞出来一个副本，避免在迭代时修改原序列可能出现问题
# numbers[l:r:step] [l,r)
for x in numbers[:] :
    if x%2==0 :
        numbers.remove(x)
print(numbers)