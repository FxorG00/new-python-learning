# 13）给定一个字典 fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}，
# 编写一个程序，找出价格最高的水果及其价格。
fruit_prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0}
kv=fruit_prices.items()
max_p=0
max_f=""
for i in kv :
    if i[1]>max_p :
        max_p=i[1]
        max_f=i[0]
print(f"价格最高的水果是 {max_f}，它的价格是 {max_p}")