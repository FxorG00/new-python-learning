# 2）创建一个空列表fruits，然后添加 "apple", "banana", "cherry", "date" 四个元素。
# 接着在列表的开始添加 "elderberry"，在 "cherry" 之前添加 "fig"，
# 并将列表的最后一个元素替换为 "grape"。
fruits=list()
# list.append(x): 在列表末尾追加 x
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
fruits.append("date")
print(fruits)
# list.insert(index,x): 在 index 处插入 x
fruits.insert(0,"elderberry")
print(fruits)
# list.index(x,start,end)
# 返回 x 在 list 的首次出现的位置，可以指定区间
cherry_index=fruits.index("cherry")
fruits.insert(cherry_index,"fig")
# for i in range(0,len(fruits)) :
#     if fruits[i]=="cherry" :
#         fruits.insert(i,"fig")
#         break
fruits[len(fruits)-1]="grape"
print(fruits)