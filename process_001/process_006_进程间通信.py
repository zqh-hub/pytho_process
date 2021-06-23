import multiprocessing
import time


def producer(q):
    for i in range(20):
        time.sleep(0.2)
        print("生产者生产了{}".format(i))
        q.put(i)


def customer(q):
    for i in range(20):
        time.sleep(0.4)
        print("消费者消费了{}".format(q.get()))


if __name__ == '__main__':
    multiprocessing.set_start_method("fork")
    qe = multiprocessing.Queue()
    lock = multiprocessing.get_context().Lock()
    p1 = multiprocessing.Process(target=producer, args=(qe,))
    p2 = multiprocessing.Process(target=customer, args=(qe,))

    p1.start()
    p2.start()
