def cal(x,y,op) :
    return op(x,y)
ans=cal(1,5,lambda x,y: x+y)
# lambda 参数: 返回的表达式
print(ans)