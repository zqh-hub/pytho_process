import threading
import time, queue

q = queue.Queue()


def p():
    for i in range(20):
        time.sleep(0.1)
        print("{}生产第{}个商品".format(threading.current_thread().name, i))
        q.put("{},{}".format(threading.current_thread().name, i))


def c():
    for i in range(20):
        time.sleep(1)
        print("消费第{}个产品".format(q.get()))


t1 = threading.Thread(target=p, name="生产者1")
t2 = threading.Thread(target=p, name="生产者2")
t3 = threading.Thread(target=p, name="生产者3")
c1 = threading.Thread(target=c, name="消费者")
t1.start()
t2.start()
t3.start()
c1.start()
