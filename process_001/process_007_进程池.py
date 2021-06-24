import multiprocessing, time
import os


def work(num):
    print("{}号，进程{}".format(num, os.getpid()))


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(work, (i,))
    pool.close()
    pool.join()
