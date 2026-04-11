# 4）有两个列表list1 = [1, 2, 3, 4, 5]和list2 = [6, 7, 8, 9, 10]，
# 将它们合并为一个新列表combined_list，并对combined_list进行降序排序
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
combined_list=list1+list2
combined_list.sort(reverse=True)
print(combined_list)