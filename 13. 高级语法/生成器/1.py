from collections.abc import Iterator
generator=(x for x in range(5) if x%2==0)
print(isinstance(generator,Iterator)) # 生成器是迭代器
print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
for i in generator:
    print(i)