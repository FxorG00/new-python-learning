import os
import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    # 从这个 Process 继承过来
    # 这样相比与 target=函数名，能够去 work 更复杂的任务
    # 调用 start 方法去启动进程，创建一个新进程，新进程调用 run
    # 并且这个新进程的父亲就是当前第一次执行这个 .py 的主进程
    # 因为新进程是在主进程执行到那行代码的时候创建的
    def run(self):
        print(f"当前进程id:{os.getpid()}，父进程 {os.getppid()}")

if __name__ == '__main__':
    for i in range(5):
        p=MyProcess()
        p.start()