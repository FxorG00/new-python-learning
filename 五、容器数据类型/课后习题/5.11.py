# 11）给定一个集合original_set = {1, 2, 3, 4, 5}，
# 编写一个程序，向集合中添加元素 6 和 7，并从集合中移除元素 3。
original_set = {1, 2, 3, 4, 5}
# set.add(x): 添加元素 x
original_set.add(6)
original_set.add(7)
# set.remove(x): 从集合中删除 x
original_set.remove(3)
print(original_set)