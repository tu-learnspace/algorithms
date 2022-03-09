"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1112

IDEA:
- mỗi địa điểm đánh dấu bằng chữ cái => có tối đa 26 đỉnh
- lưu bằng số thay vì lưu chữ cái => char - 'A' (bắt đầu từ 0)
- duyệt floyd cho graph của người trẻ &  graph của người già => tìm đc tổng min dist
- từ đỉnh của me và miguel xem lần lượt đỉnh nào = min đã tìm thì in ra
"""
INF = int(1e9)


def floyd(graph):
    for k in range(26):
        for i in range(26):
            if graph[i][k] == INF:
                continue
            for j in range(26):
                if graph[i][j] > graph[i][k] + graph[k][j] and graph[k][j] != INF:
                    graph[i][j] = graph[i][k] + graph[k][j]


while True:
    graph_young = [[INF for _ in range(26)] for _ in range(26)]
    graph_old = [[INF for _ in range(26)] for _ in range(26)]
    for i in range(26):
        graph_young[i][i] = 0
        graph_old[i][i] = 0

    n = int(input())
    if n == 0:
        break

    for i in range(n):
        line = input().split()

        u = ord(line[2]) - ord('A')
        v = ord(line[3]) - ord('A')
        w = int(line[4])

        if line[0] == 'Y':
            if line[1] == 'U':
                graph_young[u][v] = min(graph_young[u][v], w)   # vì có thể có nhiều đường từ 2 đỉnh có weight khác nhau => chọn cái min
            else:
                graph_young[u][v] = min(graph_young[u][v], w)
                graph_young[v][u] = min(graph_young[v][u], w)
        else:
            if line[1] == 'U':
                graph_old[u][v] = min(graph_old[u][v], w)
            else:
                graph_old[u][v] = min(graph_old[u][v], w)
                graph_old[v][u] = min(graph_old[v][u], w)

    floyd(graph_young)
    floyd(graph_old)

    me, miguel = input().split()
    me = ord(me) - ord('A')
    miguel = ord(miguel) - ord('A')

    min_dist = INF
    for i in range(26):
        if graph_young[me][i] + graph_old[miguel][i] <= min_dist:
            min_dist = graph_young[me][i] + graph_old[miguel][i]

    if min_dist == INF:
        print('You will never meet.')
    else:
        print(min_dist, end=' ')
        for i in range(26):
            if graph_young[me][i] + graph_old[miguel][i] == min_dist:
                print(chr(i + ord('A')), end=' ')
        print('')