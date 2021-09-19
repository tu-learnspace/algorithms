"""
https://www.spoj.com/problems/TRAFFICN/

- có n nút (đánh số 1->n), m đường đi 1 chiều giữa các nút
- danh sách k đường đi 2 chiều đc soạn ra
- chọn 1 trong số k đường đi đó để giảm thiểu nhiều nhất chi phí đi giữa s và t


"""
import heapq
MAX = 10**6 + 5
INF = int(1e9)

def dijkstra(s, graph, dist):
    dist[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))

    while len(pq):
        top = heapq.heappop(pq)
        curr_dist = top[0]
        curr_id = top[1]

        if curr_dist != dist[curr_id]:
            continue

        for neighbor in graph[curr_id]:
            if curr_dist + neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = curr_dist + neighbor[0]
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))


tc = int(input())
for _ in range(tc):
    n, m, k, s, t = map(int, input().split())

    graph_forward = [[] for _ in range(n + 1)]
    graph_backward = [[] for _ in range(n + 1)]
    dist_forward = [INF for _ in range(n + 1)]
    dist_backward = [INF for _ in range(n + 1)]

    for _ in range(m):
        d, c, l = map(int, input().split())
        graph_forward[d].append((l, c))
        graph_backward[c].append((l, d))

    dijkstra(s, graph_forward, dist_forward)
    dijkstra(t, graph_backward, dist_backward)

    ans = INF
    for _ in range(k):
        u, v, q = map(int, input().split())
        val = min(dist_forward[u] + dist_backward[v], dist_forward[v] + dist_backward[u]) + q
        ans = min(ans, val)

    if ans != INF:
        print(ans)
    else:
        print(-1)
