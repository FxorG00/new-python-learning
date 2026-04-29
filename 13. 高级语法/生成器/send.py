"""
    实现切换 gen 是在生成 0,1,2,3,4 or A,B,C,D,..
    利用 send 方法，send 发送的值会作为 yield 整个表达式的结果！
    并且接着执行！
    所以可以用 send 来控制 task_id
"""
def gen():
    task_id=0
    int_value=0
    char_value="A"
    print("我启动了！！")
    while True:
        if task_id==0:
            task_id=(yield int_value)
            # 先执行 yield int_value，返回 int_value
            # 等待 send 的结果后，赋值给 task_id
            int_value+=1
        elif task_id==1:
            task_id=(yield char_value)
            char_value=chr(ord(char_value)+1)
            # 先转 ascii，再转 unicode
g=gen()
print("~~~~~~~")
print(g.send(None)) # send(None) 来启动生成器
print("~~~~~~~")
print(g.send(0))
print(g.send(1))
print(g.send(1))
print(g.send(1))
print(g.send(1))