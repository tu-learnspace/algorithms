"""
https://www.hackerrank.com/challenges/bfsshortreach/problem

- Cho đồ thị, in đường đi ngắn nhất từ đỉnh S tới tất cả các đỉnh còn lại của đồ thị

- Input:
    + dòng 1: số lượng testcase. Mỗi test case chứa:
        + dòng 1: N-số đỉnh, M-số cạnh
        + M dòng tiếp theo chứa 2 số nguyên U, V: có cạnh nối giữa 2 đỉnh U, V
        + dòng cuối: đỉnh S-đỉnh xuất phát
- Output:
    + In ra N-1 dòng tương ứng đường đi ngắn nhất S tới tất cả các đỉnh
    + In ra đỉnh theo thứ tự tăng dần

IDEA:
- Dùng mảng dist[v] để lưu đường đi ngắn nhất từ s -> v
- Vd có cạnh nối u-v, cần tìm đường đi ngắn nhất từ s -> v = đường đi từ s -> u + 1
"""
from queue import Queue
MAX = 1000 + 5

def BFS(source, graph, dist):
    q = Queue()
    q.put(source)
    dist[source] = 0
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if dist[v] == -1:       # haven't visited
                dist[v] = dist[u] + 1
                q.put(v)


# main
if __name__ == '__main__':
    testcase = int(input())

    for _ in range(testcase):
        dist = [-1 for _ in range(MAX)]
        # visited = [False for _ in range(MAX)]  # ko cần mảng visited, vì đã có mảng dist, nếu dist = -1 đồng nghĩa với việc chưa visit
        graph = [[] for _ in range(MAX)]

        N, M = map(int, input().split())
        for _ in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        s = int(input())

        BFS(s, graph, dist)

        for i in range(N + 1):
            if i != s and i != 0:
                if dist[i] != -1:
                    print(dist[i] * 6, end=' ')
                else:
                    print(-1, end=' ')
        print('\n', end='')
