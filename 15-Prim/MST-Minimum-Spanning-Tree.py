"""
https://www.spoj.com/problems/MST/

- tìm MST

IDEA:
- có 10^4 dỉnh, 10^5 cạnh, chi phí 10^6.
- nếu mỗi cạnh đều có chi phí 10^6 => tổng chi phí = 10^6*10^4 = 10^10 vượt quá integer => lưu kiểu long/ long long
- dùng prim cải tiến (xài heap) để tối ưu
"""
import heapq
INF = 1e9

def prim(src):
    dist[src] = 0

    pq = []
    heapq.heappush(pq, (0, src))

    ans = 0         # cách 2 tính tổng chi phí, khi kết nạp đỉnh vào cây khung là cộng cạnh vô ans luôn

    while len(pq) > 0:
        u_id = heapq.heappop(pq)[1]
        if visited[u_id]:
            continue
        visited[u_id] = True        # kết nạp vào cây khung
        ans += dist[u_id]           # cộng vào kq luôn

        for neighbor in graph[u_id]:
            id = neighbor[1]
            weight = neighbor[0]
            if not visited[id] and dist[id] > weight:
                dist[id] = weight
                heapq.heappush(pq, (weight, id))

    # cách 1 tính tổng chi phí
    # ans = 0
    # for i in range(1,n+1):
    #     ans += dist[i]
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    print(prim(1))
