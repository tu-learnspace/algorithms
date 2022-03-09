"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1927


- input:
- output:

IDEA:
- dùng dijkstra
"""
import heapq
MAX = 10**5 + 5
INF = int(1e9)

def dijkstra(start):
    dist[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

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
for i in range(tc):
    graph = [[] for _ in range(MAX)]
    dist = [INF for _ in range(MAX)]
    n, m, s, t = map(int, input().split())
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((w, b))
        graph[b].append((w, a))

    dijkstra(s)

    if dist[t] != INF:
        print('Case #' + str(i+1) + ': ' + str(dist[t]))
    else:
        print('Case #' + str(i+1) + ': unreachable')
