import threading

# python 实现多任务的方式：多线程、多进程、多线程+多进程
import time


def dance():
    for i in range(200):
        print("跳舞")


def single():
    for i in range(200):
        print("唱歌")


t1 = threading.Thread(target=dance())
t2 = threading.Thread(target=single())

t1.start()
t2.start()
