"""
https://lightoj.com/problem/extended-traffic

- Có n giao lộ, giao lộ i có độ bận rộn b[i]
- có m đường 1 chiều giữa các giao lộ. mức phí đi qua 1 con đường u->v là (b[v]-b[u])^3
- có q truy vấn, mỗi truy vấn in ra chi phí nhỏ nhất đi từ giao lộ 1 đến giao lộ truy vấn đó
- nếu ko thể di chuyển đến hoặc chi phí đến < 3 thì in ra '?'

IDEA:
- trọng số của con đường có thể âm => ko thể xài dijkstra => xài bellman-ford
- tuy nhiên khi xuất hiện chu trình âm thì có thể ảnh hưởng tới các đỉnh sau chu trình đó => phải update đỉnh bị ảnh hưởng
- chạy bellman lần 1
- chạy bellman lần 2, với mỗi cạnh u,v nếu đỉnh v vẫn còn cải tiến đc nghĩa là đã có chu trình âm trước đỉnh v
=> cập nhật dist[v] = -INF (vì nếu đi qua nhiều lần chu trình âm thì nó -vô hạn)
"""
INF = int(1e9)

def bellman(s):
    dist[s] = 0

    # chạy bellman lần 1
    for _ in range(n):
        for j in range(m):
            source, target, weight = graph[j]
            if dist[source] != INF and dist[target] > dist[source] + weight:
                dist[target] = dist[source] + weight

    # chạy bellman lần 2
    for _ in range(n):
        for j in range(m):
            source, target, weight = graph[j]
            if dist[source] != INF and dist[target] > dist[source] + weight:
                dist[target] = -INF


tc = int(input())
for i in range(1, tc + 1):
    input()

    n = int(input())
    b = list(map(int, input().split()))

    graph = []
    dist = [INF] * (n + 1)
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        w = (b[v - 1] - b[u - 1]) ** 3
        graph.append((u, v, w))

    bellman(1)

    print("Case {}:".format(i))
    q = int(input())
    for _ in range(q):
        src = int(input())
        if dist[src] == INF or dist[src] < 3:
            print('?')
        else:
            print(dist[src])
