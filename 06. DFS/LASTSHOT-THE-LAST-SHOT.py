"""
https://www.spoj.com/problems/LASTSHOT/

- khi bom B1 nằm trong tầm ành hưởng của bom B2 thì khi bom B2 nổ thì bom B1 cũng sẽ kích hoạt mà nổ theo
- tìm quả bom nổ sao cho mang lại nhiều sát thương nhất (sát thương tính bằng số lg bom nổ)

- input:
    + dòng 1: N-số bom M-số quan hệ giữa các quả bom
    + M dòng tiếp theo: A B-mối quan hệ bom B nằm trong vùng ảnh hưởng của bom A
- output: mức độ sát thương

IDEA:
- xài dfs duyệt toàn bộ cây
- chạy qua từng nút rồi tính độ dài nhất (giống như kiểu cho từng quả bom nổ, xem bom nào nổ nhiều nhất) => reset visited cho từng node

- xài bfs bị time limit?
"""
MAX = 10**5 + 5

def dfs(src, graph, visited):
    size = 1
    s = []
    visited[src] = True
    s.append(src)

    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                size += 1
                visited[v] = True
                s.append(v)
    return size

if __name__ == '__main__':
    graph = [[] for _ in range(MAX)]
    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)

    size = 0
    for i in range(1, N+1):
        visited = [False] * (N+1)
        tmp = dfs(i, graph, visited)
        size = max(size, tmp)

    print(size)

