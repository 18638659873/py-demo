# 创建多进程
from multiprocessing import Process


def func():
    for i in range(100):
        print("func", i)


if __name__ == '__main__':
    p = Process(func())
    p.start()

    for i in range(100):
        print("main", i)
