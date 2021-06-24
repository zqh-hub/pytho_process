import threading
import time

x = 0


def work(a, b):
    time.sleep(2)
    global x
    x = a + b


t = threading.Thread(target=work, args=(1, 1))
t.start()
t.join()  # 主线程等待子线程
print(x)
