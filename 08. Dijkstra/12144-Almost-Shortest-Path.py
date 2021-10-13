"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3296

- sho đồ thị 1 chiều N đỉnh, M cạnh.
- đường đi gần ngắn nhất là ngắn liền sau đường đi ngắn nhất & tất cả các cạnh trên đường đi gần ngắn nhất này ko đc thuộc đường đi ngắn nhất
- tìm độ dài đường đi gần ngắn nhất từ đỉnh S đến D, ko có thì in ra -1 (nghĩa là phải đi qua đường ngắn nhất)

IDEA:
- vì đường đi gần ngắn nhất ko đc chứa đường đi ngắn nhất
=> xóa các cạnh thuộc đường đi ngắn nhất ra khỏi đồ thị
- sau đó dijkstra trên đồ thị mới để tìm đường đi ngắn nhất

- làm sao biết 1 cạnh thuộc đường đi ngắn nhất hay k?
- giả sử ngắn nhất từ s -> d đi qua u-v
=> nghĩa là xét ngắn nhất từ s -> u + ngắn nhất từ d -> u + u-v == ngắn nhất s -> d
=> dist_s[u] + |(u, v)| + dist_d[v] == dist_s[d]
=> lần lượt xét các cặp u-v thỏa mãn thì xóa nó khỏi đồ thì

- đầu tiên dijkstra từ s => tìm đc ngắn nhất từ s tới các đỉnh còn lại
- đổi chiều đồ thị rồi dijkstra từ d => tìm đc ngắn nhất từ d tới các đỉnh còn lại (vì là đồ thị có hướng, ta ko nên dijkstra mỗi đỉnh rồi xem dist của nó đến d đc => tốn kém)
"""
from heapq import heappush, heappop
INF = 1e9

def dijkstra(src, graph, dist):
    pq = []
    heappush(pq, (0, src))
    dist[src] = 0

    while len(pq) > 0:
        curr_dist, curr_id = heappop(pq)

        if curr_dist != dist[curr_id]:
            continue

        for neighbor_dist, neighbor_id in graph[curr_id]:
            if dist[neighbor_id] > neighbor_dist + curr_dist:
                dist[neighbor_id] = neighbor_dist + curr_dist
                heappush(pq, (dist[neighbor_id], neighbor_id))



while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph_new = [[] for _ in range(n)]      # đồ thị mới (xóa đi các đường đi ngắn nhất)
    graph_s = [[] for _ in range(n)]        # dijkstra từ đỉnh s
    graph_d = [[] for _ in range(n)]        # đồ thị ngược để dijkstra từ đỉnh d
    dist_new = [INF] * n
    dist_s = [INF] * n
    dist_d = [INF] * n

    s, d = map(int, input().split())

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph_s[u].append((w, v))           # đồ thị gốc
        graph_d[v].append((w, u))           # đồ thị ngược

    dijkstra(s, graph_s, dist_s)
    dijkstra(d, graph_d, dist_d)

    # tạo đồ thì từ những cạnh ko phải thuộc đường đi ngắn nhất ngắn nhất (dùng giả sử ngắn từ s -> d đi qua u-v, ai phạm giả sử thì nhận)
    for u in range(n):
        for w, v in graph_s[u]:
            if dist_s[u] + w + dist_d[v] != dist_s[d]:
                graph_new[u].append((w, v))

    dijkstra(s, graph_new, dist_new)

    if dist_new[d] != INF:
        print(dist_new[d])
    else:
        print(-1)