"""
- Tìm đường đi bằng DFS dùng đệ quy
- Cách cài đặt DFS bằng stack thì y chang BFS chỉ thay queue bằng stack
- Nếu cài bằng đệ quy thì phải đưa việc set False cho visited và path ra toàn cục
"""

from queue import Queue

MAX = 100
V = None
E = None
visited = [False for _ in range(MAX)]   # mảng lưu vết: đỉnh nào đã visited thì true, ko thì false => để khỏi xét lại
path = [0 for _ in range(MAX)]  # mảng lưu path (path là đỉnh kề trước) => khi truy vết thì xài
graph = [[] for _ in range(MAX)]  # mảng lưu lại các mảng con là đỉnh kề với đỉnh i (đồ thì đề bài) => để biết mà xét đinh nào (push nào vô queue)

# dùng stack
def DFS(src):
    for i in range(V):          # nếu dùng stack thì đoạn này ko cần lặp lại ở main
        visited[i] = False
        path[i] = -1
    s = []
    visited[src] = True
    s.append(src)
    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                path[v] = u

# dùng đệ quy
def DFSRecursion(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            DFSRecursion(v)


def printPathRecursion(s, f):
    if s == f:
        print(f, end=' ')
    else:
        if path[f] == -1:
            print('No path')
        else:
            printPathRecursion(s, path[f])
            print(f, end=' ')


if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    s = 0
    f = 5

    # dont need this if using BFS/DFS-stack
    for i in range(V):
        visited[i] = False
        path[i] = -1
    # => BFS/DFS-stack thì block này quăng vô hàm lun

    DFSRecursion(s)
    printPathRecursion(s, f)

# vd
# input :
# 6 8
# 0 1
# 0 3
# 1 2
# 1 3
# 1 5
# 2 5
# 3 4
# 3 5
# output: 0 1 2 5