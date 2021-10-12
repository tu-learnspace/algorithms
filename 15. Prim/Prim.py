"""
- Prim khá giống Dijkstra. Khác nhau ở chỗ:
+ Dijkstra: xét Chi phí đường đi trc đó + chi phí đường đi tới đỉnh khác < chi phí đường đi tốt nhất hiện tại -> rồi mới quyết định đi hay k
+ Prim    : xét                           chi phí đường đi tới đỉnh khác < chi phí tốt nhất hiện tại

Vd Dijkstra là xét u,v thì xét từ s -> u + u-v có là tốt nhất ko
còn Prim ko cần xét đường đi trc đó, chỉ xét CHI PHÍ CẠNH hiện tại (vì đang chọn ra cây khung nên đi từ đỉnh nào cũng z) => ko xét lại đường đi đã đi qua

- Prim hoạt động đc trên đồ thị âm dương tùy ý. Vì với đồ thị V đỉnh luôn luôn có V-1 cạnh
=> Prim luôn chọn ra V-1 cạnh ko tạo chu trình (khác vs Dijkstra chỉ xài đồ thị ko âm)
- Đồ thị xài Prim mặc định là vô hướng (vì tìm cây khung mà)
- Nên lưu dạng edge list (danh sách kề). Nên lấy đỉnh đầu = 0 cho dễ xử lý (đỉnh nào cũng đc)
"""
import heapq        # tìm minimum => min heap
INF = 1e9

# class Node:
#     def __init__(self, id, dist):
#         self.dist = dist
#         self.id = id
#     def __lt__(self, other):
#         return self.dist <= other.dist
#
# hoặc dùng tuple lưu (chi phí, đỉnh) (vì tuple python mặc định so sánh cái đầu trc)


def printMST():
    ans = 0
    for i in range(n):          # duyệt qua từng đỉnh
        if path[i] == -1:       # có đỉnh nối trong cây khung
            continue
        ans += dist[i]
        print('{0} - {1}: {2}'.format(path[i], i, dist[i]))
    print('Weight of MST: {0}'.format(ans))

def prims(src):
    pq = []                         # min heap
    heapq.heappush(pq, (0, src))    # chi phí tại src là đứng tại chỗ
    dist[src] = 0
    while len(pq) > 0:
        top = heapq.heappop(pq)
        u = top[1]                  # id

        if visited[u]:              # tránh TH xét lại (TH nút cổ chai), ở đây kiểm tra dist (w = top[0]) cũng đc
            continue
        visited[u] = True

        for neighbor in graph[u]:
            v = neighbor[1]     # id
            w = neighbor[0]     # weight
            if not visited[v] and w < dist[v]:
                dist[v] = w
                heapq.heappush(pq, (w, v))
                path[v] = u


if __name__ == '__main__':
    n, m = map(int, input().split())        # số đỉnh, số cạnh
    graph = [[] for _ in range(n)]          # lưu (đỉnh kề, trọng số)
    dist = [INF for _ in range(n)]          # lưu chi phí đường đi tới đỉnh đó
    path = [-1 for _ in range(n)]           # optional: lưu vết đường đi - đỉnh trc đỉnh đó
    visited = [False for _ in range(n)]     # đánh dấu những đỉnh nào đã thuộc cây khung rồi thì ko xét lại (khởi đầu = false): vì ban đầu xét tử 1 điểm ta đã tham lam chọn cái tốt nhất rồi

    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    prims(0)
    printMST()


# input
# 6 9
# 0 1 -2
# 0 3 9
# 1 2 3
# 1 3 8
# 1 4 5
# 1 5 -1
# 2 5 5
# 3 4 3
# 4 5 7

# output
# 0 - 1: -2
# 1 - 2: 3
# 4 - 3: 3
# 1 - 4: 5
# 1 - 5: -1
# Weight of MST: 8