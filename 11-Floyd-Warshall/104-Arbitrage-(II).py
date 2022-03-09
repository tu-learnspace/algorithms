"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=377

"""
INF = int(1e9)


def transform_name(nm):
    for idx, name in enumerate(names):
        if name == nm:
            return idx


def floyd():
    for k in range(n):
        for i in range(n):
            if graph[i][k] == -INF:
                continue
            for j in range(n):
                if graph[k][j] != -INF and graph[i][j] < graph[i][k]*graph[k][j]:
                    graph[i][j] = graph[i][k]*graph[k][j]

case = 1
while True:
    n = int(input())
    if n == 0:
        break
    names = []
    graph = [[-INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        names.append(input())
        graph[i][i] = 1     # tự là chính nó

    m = int(input())
    for _ in range(m):
        line = list(input().split())

        source = transform_name(line[0])
        w = float(line[1])
        target = transform_name(line[2])

        graph[source][target] = w

    floyd()

    check = False
    for i in range(n):
        if graph[i][i] > 1:
            check = True

    print('Case {}:'.format(case), end=' ')
    if check:
        print('Yes')
    else:
        print('No')
    case += 1

    input()
