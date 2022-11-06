# python中实现多线程
from threading import Thread

from concurrent.futures import ThreadPoolExecutor


def func(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    t = Thread(func("thread1"), args="threadName", )
    t.start()

    for i in range(1000):
        print("main", i)

    # 线程池
    with ThreadPoolExecutor(10) as t:
        t.submit(func(), "param")
        # 回调函数，接受返回值结果
        t.submit(func(), "callback").add_done_callback(fn=func())


# 自定义类，继承Thread
class MyThread(Thread):
    # 初始化函数
    def __init__(self, name):
        # 调用父类的初始化函数
        super(MyThread, self).__init__()
        self.name = name

    # 线程的run方法
    def run(self):
        # todo
        pass
