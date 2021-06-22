import threading
import time

ticket = 100
lock = threading.Lock()


def sell_ticket():
    global ticket
    while True:
        lock.acquire()  # 加同步锁
        if ticket > 0:
            ticket -= 1
            lock.release()  # 每执行完一个卖票的动作就放开
            print("{},此时ticket是：{}".format(threading.current_thread().name, ticket))
        else:
            lock.release()  # 所有的票卖完了，锁释放开
            print("没票了")
            break


t1 = threading.Thread(target=sell_ticket, name="线程1")
t2 = threading.Thread(target=sell_ticket, name="线程2")
t3 = threading.Thread(target=sell_ticket, name="线程3")
t1.start()
t2.start()
t3.start()
