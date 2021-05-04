import multiprocessing
from multiprocessing import Process


def saturate(i):
    while True:
        i = i * 2


if __name__ == '__main__':
    ps = []
    for i in range(multiprocessing.cpu_count()):
        p = Process(target=saturate, args=(i, ))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
