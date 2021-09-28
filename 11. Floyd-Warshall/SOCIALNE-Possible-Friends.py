"""
https://www.spoj.com/problems/SOCIALNE/

- 2 người là possible friend khi:
    + họ ko phải là bạn bè
    + họ có ít nhất 1 bạn chung
- tìm người có possible friend nhiều nhất và số lượng possible friend của ng đó

IDEA:
- xem mỗi người là nút
- để 2 người là possible friend thì họ ko phải là bạn (ko có cạnh nối trực tiếp) và đường đi của họ đúng bằng 2
- nếu 2 người có đường nối trực tiếp thì đường đi ngắn nhất của họ = 1
=> chỉ cần tìm đường đi ngắn nhất và ktra coi có = 2 ko
=> nghĩa là tìm khoảng cách giữa mọi cặp đỉnh trong đồ thì => chạy thuật toán floyd
"""
INF = int(1e9)


def floyd():
    for k in range(M):
        for i in range(M):
            if graph[i][k] == INF:
                continue
            for j in range(M):
                if graph[k][j] != INF and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


tc = int(input())
for _ in range(tc):
    first_line = list(input())
    M = len(first_line)
    graph = [[None for _ in range(M)] for _ in range(M)]
    graph[0] = first_line
    for i in range(1, M):
        graph[i] = list(input())

    for i in range(M):
        for j in range(M):
            if i == j:
                graph[i][j] = 0
            elif graph[i][j] == 'N':
                graph[i][j] = INF
            elif graph[i][j] == 'Y':
                graph[i][j] = 1

    floyd()

    max_friend = id_ = 0
    for i in range(M):      # xét mỗi người (mỗi dòng của graph), xem cái nào = 2 (nghĩa bạn ngắn nhất = 2) thì tăng possible friend lên
        count = 0
        for j in range(M):
            if graph[i][j] == 2:
                count += 1
        # update max
        if count > max_friend:
            max_friend = count
            id_ = i

    print(id_, max_friend)
