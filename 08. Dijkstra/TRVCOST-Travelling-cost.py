"""
https://www.spoj.com/problems/TRVCOST/

- có 501 địa điểm (0 -> 500)
- có n con đường nối các địa điểm vs chi phí
- tìm chi phí thấp nhất đi từ u -> q

- input:
    + dòng 1: N-số đường cần tìm
    + n dòng tiếp theo, mỗi dòng: A B W (đường đi từ A->B có chi phí W)
    + dòng tiếp theo: U-nơi bắt đầu
    + dòng tiếp theo: Q-số nơi kết thúc
    + Q dòng còn lại, mỗi dòng: nơi kết thúc
- output: chi phí thấp nhất để đi từ U tới các nơi khác. ko đc thì 'NO PATH'

IDEA:
- dùng dijkstra
"""
import heapq
MAX = 501
INF = int(1e9)
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]

def dijkstra(start):
    pq = []
    dist[start] = 0
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

n = int(input())
for i in range(n):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

start = int(input())
dijkstra(start)

n_end = int(input())
for _ in range(n_end):
    end = int(input())
    if dist[end] != INF:
        print(dist[end])
    else:
        print('NO PATH')