"""
    为了防止在函数里面修改到函数外面的 list0
"""

import copy

def change_list(list1) :
    list1[3].append(40)
# list0[3] 这个变量 指向 [10,20,30] 这个对象
list0=[1,2,3,[10,20,30]]
list00=copy.deepcopy(list0)
# list00=copy.deepcopy(list0)
print(f"调用前的list0:{list0}")
print(f"调用前的list00:{list00}")
change_list(list00)
print(f"调用后的list0:{list0}")
print(f"调用后的list00:{list00}")

