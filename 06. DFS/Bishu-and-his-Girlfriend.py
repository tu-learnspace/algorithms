"""
https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/

- có các vương quốc nối vs nhau có hình dạng cây đồ thị
- Bishu ở vương quốc 1 (đỉnh gốc của đồ thị cây)
- có Q cô gái sống ở quốc gia lân cận. Bishu muốn chọn vợ ở gần nhất, nếu có nhìu ng như v thì chọn id nhỏ hơn

- Input:
    + dòng 1: N-số vương quốc
    + N-1 dòng tiếp theo có dạng u-v (có cạnh từ đỉnh u -> v)
    + dòng tiếp theo: Q-số cô gái muốn ứng cử làm vợ
    + Q dòng tiếp theo: x-id của vương quốc mà các cô gái đó sống
- Output: id của cô gái mà Bishu sẽ lấy

IDEA:
- vì đây là đồ thị dạng cây, liên thông (2 đỉnh chỉ có 1 cạnh)
=> BFS/DFS có thể chỉ ra đường đi này & là đường đi ngắn nhất luôn
- chạy DFS từ nhà Bishu đến các nhà còn lại (hoàn thiện mảng dist) rồi tìm cái min trong dist
"""
import sys
sys.setrecursionlimit(10 ** 6)

MAX = 1000 + 5
graph = [[] for _ in range(MAX)]
dist = [-1 for _ in range(MAX)]
visited = [False for _ in range(MAX)]


def DFS(src):
    for v in graph[src]:
        if not visited[v]:
            dist[v] = dist[src] + 1
            visited[v] = True
            DFS(v)


if __name__ == '__main__':
    N = int(input())
    for _ in range(N - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist[1] = 0
    visited[1] = True
    DFS(1)

    M = int(input())
    min_dist = min_id = N + 1  # max distance
    for _ in range(M):
        id = int(input())
        if dist[id] < min_dist or (dist[id] == min_dist and id < min_id):
            min_dist = dist[id]
            min_id = id

    print(min_id)