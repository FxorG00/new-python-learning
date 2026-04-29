import time
import multiprocessing

def write_file():
    count=0
    with open("test.txt","a") as f:
        while True:
            count+=1
            f.write(f"{count} hello world\n")
            f.flush()
            time.sleep(0.1)

def read_file():
    with open("test.txt","r") as f:
        while True:
            time.sleep(0.1)
            print(f.readline())

if __name__ == '__main__':
    p1=multiprocessing.Process(target=write_file)
    # 创建一个进程
    p2=multiprocessing.Process(target=read_file)
    # 创建一个进程
    p1.start()
    p2.start()