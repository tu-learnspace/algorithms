"""
https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/successful-marathon-0691ec04/


IDEA:

"""
import heapq
MAX = 10**6 + 5
INF = int(1e9)
graph = [[] for _ in range(MAX)]


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



n, m, k, x = map(int, input().split())
choco_cities = list(map(int, input().split()))

for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u].append((d, v))
    graph[v].append((d, u))
a, b = map(int, input().split())

dist1 = [INF for _ in range(MAX)]
dijkstra(a, dist1)
dist2 = [INF for _ in range(MAX)]
dijkstra(b, dist2)

ans = INF
for i in range(k):
    if dist2[choco_cities[i]] <= x:
        ans = min(ans, dist1[choco_cities[i]] + dist2[choco_cities[i]])

if ans != INF:
    print(ans)
else:
    print('-1')
