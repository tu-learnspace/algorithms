"""
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1744

- cho tọa độ các điểm
- tính khoảng cách ngắn nhất giữa 2 điểm bất kỳ. tìm khoảng cách có giá trị lớn nhất
- chỉ xét những cặp điểm có khoảng cách giữa 2 điểm ko vượt quá 10

IDEA:
- floyd bth
"""
import math
INF = int(1e9)


def floyd():
    for k in range(n):
        for i in range(n):
            if graph[i][k] == INF:
                continue
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j] and graph[k][j] != INF:
                    graph[i][j] = graph[i][k] + graph[k][j]


tc = int(input())
for t in range(tc):
    n = int(input())
    graph = [[INF for _ in range(n)] for _ in range(n)]

    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)

    for i in range(n):
        for j in range(n):
            dist = math.sqrt((xs[i] - xs[j]) ** 2 + (ys[i] - ys[j]) ** 2)   # khoảng cách giữa 2 điểm
            if dist <= 10:
                graph[i][j] = dist

    floyd()

    print('Case #{}:'.format(t + 1))
    max_dist = -INF
    for i in range(n):
        for j in range(n):
            if graph[i][j] > max_dist:
                max_dist = graph[i][j]
    if max_dist == INF:
        print('Send Kurdy')
    else:
        print('{:.4f}'.format(max_dist))

    print()

