"""
https://open.kattis.com/problems/shortestpath3

- có 4 số n, m, q, s
    n: số đỉnh đồ thị có hướng (đánh dấu từ 0 -> n-1)
    m: số cạnh
    q: số truy vấn
    s: vị trí đỉnh xuất phát
- với mỗi truy vấn, in ra khoảng cách ngắn nhất từ đỉnh s tới đỉnh mà truy vấn đó yêu cầu
- nếu ko đc thì in Impossible, -Infinity nếu có thể đi đc từ s tới đỉnh đó bằng con đường ngắn vô hạn

IDEA:
- tìm đường đi ngắn nhất từ 1 đỉnh đến tất cả các đỉnh còn lại => bellman
- con đường ngắn vô hạn => tìm chu trình âm => bellman & check chu trình âm
- nếu phát hiện chu trình âm, hãy phát hiện tất cả các cạnh thuộc chu trình âm
=> check chu trình âm phải lặp 2 vòng for (vì 1 vòng for chỉ tìm đc 1 cạnh thuộc chu trình âm) => bellman 2 lần
"""
INF = 1e9


def bellman(src):
    dist[src] = 0

    for _ in range(1, n):
        improver = False
        for source, target, weight in graph:
            if dist[source] != INF and dist[source] + weight < dist[target]:
                dist[target] = dist[source] + weight
                improver = True
        if not improver:
            break

    for _ in range(1, n):           # đảm bảo tất cả các đỉnh bị ảnh hưởng bởi chu trình âm đều được đánh dấu
        for source, target, weight in graph:
            if dist[source] != INF and dist[source] + weight < dist[target]:    # vẫn cải tiến đc
                dist[target] = -INF                                             # đánh dấu có chu trình âm


while True:
    n, m, q, s = map(int, input().split())
    if n == 0:
        break

    graph = []
    dist = [INF] * n

    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    bellman(s)

    for _ in range(q):
        e = int(input())

        if dist[e] == INF:
            print("Impossible")
        elif dist[e] == -INF:
            print("-Infinity")
        else:
            print(dist[e])

    print()
