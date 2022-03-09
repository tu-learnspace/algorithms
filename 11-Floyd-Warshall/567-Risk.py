"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=508


"""
INF = int(1e9)


def floyd():
    for k in range(21):
        for i in range(21):
            if graph[i][k] == INF:
                continue
            for j in range(21):
                if graph[i][j] > graph[i][k] + graph[k][j] and graph[k][j] != INF:
                    graph[i][j] = graph[i][k] + graph[k][j]


tc = 1
while True:
    try:
        graph = [[INF for _ in range(21)] for _ in range(21)]
        for i in range(21):
            graph[i][i] = 0

        for i in range(1, 20):
            line = list(input().split())
            n = int(line[0])
            for j in range(1, n + 1):
                graph[i][int(line[j])] = 1
                graph[int(line[j])][i] = 1

        floyd()

        print('Test Set #{}'.format(tc))
        q = int(input())
        for _ in range(q):
            start, end = map(int, input().split())
            print('{:2d} to {:2d}: {}'.format(start, end, graph[start][end]))
        tc += 1
        print('')

    except EOFError:
        break
