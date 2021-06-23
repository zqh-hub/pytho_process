##### python 进程

###### 多线程实现

```python
import threading
import time

# python 实现多任务的方式：多线程、多进程、多线程+多进程
def dance():
    for i in range(200):
        print("跳舞")

def single():
    for i in range(200):
        print("唱歌")

t1 = threading.Thread(target=dance())  # 多线程
t2 = threading.Thread(target=single())

t1.start()
t2.start()
```

###### 多线程卖票

```python
import threading
import time

ticket = 100
lock = threading.Lock() # 创建锁


def sell_ticket():
    global ticket
    while True:
        lock.acquire()  # 加"同步锁"
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
```

###### 线程间通信

```python
import threading
import time, queue

q = queue.Queue()  # 创建队列


def p(n):
    for i in range(n):
        time.sleep(0.1)
        print("{}生产第{}个商品".format(threading.current_thread().name, i))
        q.put("{},{}".format(threading.current_thread().name, i))  # 放入队列


def c(m):
    for i in range(m):
        time.sleep(1)
        print("消费第{}个产品".format(q.get()))  # 从队列中获取，根据“先进先出”的特点，先生产的先消费


t1 = threading.Thread(target=p, name="生产者1", arg=(20,))
t2 = threading.Thread(target=p, name="生产者2", arg=(20,))
t3 = threading.Thread(target=p, name="生产者3", arg=(20,))
c1 = threading.Thread(target=c, name="消费者", arg=(20,))

t1.start()
t2.start()
t3.start()
c1.start()
```

###### 多进程实现

```python
import multiprocessing
import time
def dance(n):
    for i in range(n):
        time.sleep(0.3)
        print("跳舞")
def sing(m):
    for i in range(m):
        time.sleep(0.3)
        print("唱歌")
if __name__ == '__main__':
    # target:目标程序
    # arg:用来传参，一个元组
    p1 = multiprocessing.Process(target=dance, args=(20,))  # 多进程
    p2 = multiprocessing.Process(target=sing, args=(20,))
    p1.start()
    p2.start()
```

###### 线程与进程之间的关系

```
同一进程间的不同线程可以共享全局变量，不同的进程之间不能共享全局变量
一个程序至少要有一个进程(主进程)，一个进程至少有一个线程(主线程)
线程不能独立执行，必须依赖进程
```

###### 进程间通信

```python
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
    multiprocessing.set_start_method("fork")  # 这里是因为Mac默认启动程序的方式是：fork,python解释器的默认方式是spawn,所以需要指定
    qe = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(qe,))
    p2 = multiprocessing.Process(target=customer, args=(qe,))

    p1.start()
    p2.start()
```

