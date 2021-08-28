"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3359

"""
from queue import Queue

case = 1
while 1:
    p, c = map(int, input().split())
    if p == 0 and c == 0:
        break

    print('Case', case, end='')
    print(':')
    case += 1

    q = Queue()
    prior = Queue()
    deleted_prior = False

    for i in range(p):
        q.put(i + 1)

    for i in range(c):
        N = input()

        if N == 'N':
            if prior.empty():

            else:
                value = q.get()
                if value == piority:
                    value = q.get()
                    piority = 0
                    print('get rid of piore')
                print(value)
                q.put(value)
        else:
            value = int(N.split()[1])
            prior.put(value)


