"""
https://www.spoj.com/problems/SHPATH/

- input:
- output:

IDEA:
- xài dijkstra bình thường
"""
import heapq
MAX = 10**5 + 5
INF = int(1e9)
cities = dict()     # map city with id

def dijkstra(s):
    pq = []
    dist[s] = 0
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
    graph = [[] for _ in range(MAX)]

    n_city = int(input())
    city_id = 0
    for _ in range(n_city):
        city_id += 1
        city_name = input()
        cities[city_name] = city_id
        e = int(input())
        for _ in range(e):
            nct, cost = map(int, input().split())
            graph[city_id].append((cost, nct))

    r = int(input())
    for _ in range(r):
        dist = [INF for _ in range(MAX)]
        name1, name2 = input().split()
        city1, city2 = cities[name1], cities[name2]
        dijkstra(city1)
        print(dist[city2])
    blank = input()