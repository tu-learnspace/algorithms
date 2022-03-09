"""
https://lightoj.com/problem/commandos

IDEA:
- hai tòa nhà liên thông bởi nhiều nhất một con đường => đồ thị dạng cây
=> tìm đường từ vị trí xuất phát đến nút lá + đường từ nút lá tới vị trí kết thúc
- dùng dijkstra tìm đường đi ngắn nhất đến các nút => nút lá là nút có đường đi xa nhất
"""
import heapq
MAX = 10**5 + 5
INF = int(1e9)


def dijkstra(s, dist):
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
for t in range(tc):
    graph = [[] for _ in range(MAX)]
    n = int(input())
    r = int(input())
    for _ in range(r):
        u, v = map(int, input().split())
        graph[u].append((1, v))
        graph[v].append((1, u))

    s, d = map(int, input().split())

    dist1 = [INF for _ in range(MAX)]
    dijkstra(s, dist1)
    dist2 = [INF for _ in range(MAX)]
    dijkstra(d, dist2)

    total = 0
    for i in range(n):
        total = max(total, dist1[i] + dist2[i])

    print('Case ' + str(t+1) + ':', total)
