class MyIterator:
    def __init__(self,data):
        self.data=data
        self.index=0
    def __iter__(self):
        print("wowowow")
        return self
    def __next__(self):
        print("hihihi")
        if self.index==len(self.data):
            raise StopIteration
        self.index+=1
        return self.data[self.index-1]
f=MyIterator([10,20,30,40])
for k in f:
    print(k)
# 等价于
# k=f.__iter__()
# print(next(k))