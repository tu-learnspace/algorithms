"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=499

- Coi lỗ sâu là con đường, hệ sao là đỉnh
- Cho đồ thị có hướng, n đỉnh m cạnh (có thể âm)
- Luôn có đường đi từ đỉnh 0 đến tất cả đỉnh còn lại
- Giữa 2 đỉnh luôn có nhiều nhất 1 cạnh => đồ thị đơn, không có khuyên
- Hòi có chu trình âm không?

IDEA:
- hỏi có chu trình âm thì dùng bellmanford basic thôi
"""
INF = int(1e9)
def bellman(s):
    dist = [INF]*n
    dist[s] = 0
    for i in range(n):
        for j in range(m):
            src = graph[j][0]
            tar = graph[j][1]
            wg = graph[j][2]
            if dist[src] != INF and dist[src] + wg < dist[tar]:
                dist[tar] = dist[src] + wg

    for j in range(m):
        src = graph[j][0]
        tar = graph[j][1]
        wg = graph[j][2]
        if dist[src] != INF and dist[src] + wg < dist[tar]:
            dist[tar] = dist[src] + wg
            return False

    return True


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    graph = []
    for _ in range(m):
        x, y, t = map(int, input().split())
        graph.append((x, y, t))

    if not bellman(0):
        print('possible')
    else:
        print('not possible')
