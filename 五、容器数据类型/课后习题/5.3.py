# 3）给定一个列表 prices = [10.5, 20.0, 15.75, 8.2, 12.0]，
# 编写一个程序，将列表中的元素都乘以 1.1（表示增加 10%），
# 并将结果存储在一个新列表new_prices中。
prices=[10.5, 20.0, 15.75, 8.2, 12.0]
new_prices=list()
for x in prices:
    # round 用于保留几位小数
    new_prices.append(round(x*1.1,2))
print(new_prices)