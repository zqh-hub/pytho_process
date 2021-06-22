import multiprocessing
import time, os


def dance(n):
    for i in range(n):
        print("dance----", os.getpid())
        time.sleep(0.3)
        print("跳舞")


def sing(m):
    for i in range(m):
        print("sing-----", os.getpid())
        time.sleep(0.3)
        print("唱歌")


if __name__ == '__main__':
    # target:目标程序
    # arg:用来传参，一个元组
    p1 = multiprocessing.Process(target=dance, args=(20,))
    p2 = multiprocessing.Process(target=sing, args=(20,))
    p1.start()
    p2.start()
