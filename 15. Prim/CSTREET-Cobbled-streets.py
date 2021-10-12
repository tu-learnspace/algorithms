"""
https://www.spoj.com/problems/CSTREET/

- Prim bình thường, sau đó lấy chi phí nhân cho price
"""
import heapq
INF = 1e9

def prim(src, price):
    dist[src] = 0

    pq = []
    heapq.heappush(pq, (0, src))

    ans = 0

    while len(pq) > 0:
        u_id = heapq.heappop(pq)[1]
        if visited[u_id]:
            continue
        visited[u_id] = True
        ans += dist[u_id]

        for neighbor in graph[u_id]:
            id = neighbor[1]
            weight = neighbor[0]
            if not visited[id] and dist[id] > weight:
                dist[id] = weight
                heapq.heappush(pq, (weight, id))

    return ans*price

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        p = int(input())

        n = int(input())
        m = int(input())

        graph = [[] for _ in range(n + 1)]
        dist = [INF for _ in range(n + 1)]
        visited = [False for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            graph[u].append((w, v))
            graph[v].append((w, u))

        print(prim(1, p))
