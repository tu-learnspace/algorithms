"""
Source code BFS
"""
# basic
from queue import Queue
MAX = 100
V = None
E = None
visited = [False for i in range(MAX)]   # Mảng lưu vết là đỉnh nào đã visit thì true, ko thì false
                                        # => để khỏi xét lại nữa khi modify mảng path
path = [0 for i in range(MAX)]          # Mảng lưu lại path của đỉnh i (path là đỉnh kề trc i trong đường đi)
                                        # => khi truy vết lại thì xài
graph = [[] for i in range(MAX)]        # Mảng lưu lại các mảng là đỉnh kề với đỉnh i
                                        # => từ đây mới biết phải xét đỉnh nào khi modify path

# Thuật toán chính, s là đỉnh gốc
def BFS(s):
    for i in range(V):              # Khởi tạo
        visited[i] = False
        path[i] = -1
    q = Queue()                     # Queue để push vào những đỉnh cần xét
    # Bắt đầu từ đỉnh gốc
    visited[s] = True
    q.put(s)
    # Loang ra
    while not q.empty():
        u = q.get()                 # lấy đỉnh u ra khỏi queue để xét
        for v in graph[u]:          # xét các đỉnh kề với đỉnh u
            if not visited[u]:
                visited[v] = True   # đánh dấu đã thăm
                q.put(v)            # thêm vào queue (để lát vòng while sau xét - loang ra)
                path[v] = u         # đánh dấu đỉnh trc v là u



# In đường đi từ s -> f (dùng đề quy)
def printPath(s, f):
    if s == f:
        print(f, end=' ')
    else:
        if path[f] == -1:
            print('No path')
        else:
            printPath(s, path[f])    # từ trước f -> s
            print(f, end=' ')


if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)            # đồ thị không hướng
        graph[v].append(u)

    s = 0
    f = 1
    BFS(s)
    printPath(s, f)
