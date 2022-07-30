from concurrent.futures import ThreadPoolExecutor
import threading


class A:

    __lock__: threading.Lock = threading.Lock()
    __count__: int = 0

    def __init__(self):
        pass

    def Run(self):
        self.__lock__.acquire()
        self.__count__ = self.__count__ + 1
        self.__lock__.release()
        print(
            f'{ threading.current_thread () } calc { id(self) } count={self.__count__}\n')


def RunTest():
    print(
        f'{ threading.current_thread () } Run \n')


if __name__ == '__main__':

    a1 = A()
    a2 = A()

    tp = ThreadPoolExecutor(5)
    tp.submit(a1.Run)
    # tp.submit(fn=a1.Run())
    tp.submit(RunTest)
    tp.shutdown(True)
