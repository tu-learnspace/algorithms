"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1876

"""
from queue import Queue

while 1:
    n = int(input())
    if n == 0:
        break

    q = Queue()
    for i in range(1, n + 1, 1):
        q.put(i)

    if q.qsize() == 1:
        print('Discarded cards:', end='')
    else:
        print('Discarded cards: ', end='')

    while q.qsize() != 1:
        if q.qsize() == 2:
            print(q.get(), end='')
        else:
            print(q.get(), end=', ')
        value = q.get()
        q.put(value)
    print("\nRemaining card:", q.queue[0])
