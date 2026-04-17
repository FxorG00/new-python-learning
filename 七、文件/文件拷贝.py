"""
E 盘有一个 doubao.png
我要把它在 D 盘也复制一份
"""

def copy(source_path,dest_path) :
    source_file=open(source_path,"rb")
    dest_file=open(dest_path,"wb")
    content=source_file.read()
    dest_file.write(content)
    dest_file.close()
    source_file.close()

copy("E:/doubao.png","D:/doubao.png")
