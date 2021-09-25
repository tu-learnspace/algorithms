"""
- Tìm đường đi bằng BFS
- Hàm BFS giúp hoàn thiện bảng path & visited => từ path trace ngc ra đường đi
"""

from queue import Queue

MAX = 100
V = None
E = None
visited = [False for _ in range(MAX)]   # mảng lưu vết: đỉnh nào đã visited thì true, ko thì false => để khỏi xét lại
path = [0 for _ in range(MAX)]          # mảng lưu path (path là đỉnh kề trước) => khi truy vết thì xài
graph = [[] for _ in range(MAX)]        # mảng lưu lại các mảng con là đỉnh kề với đỉnh i (đồ thì đề bài) => để biết mà xét đinh nào (push nào vô queue)

# thuật toán để lưu trữ đồ thị & đường đi, s là đỉnh gốc
def BFS(s):
    for i in range(V):          # khởi tạo
        visited[i] = False
        path[i] = -1
    q = Queue()                 # queue để push vào những đỉnh cần xét (kề vs đỉnh hiện tại và not visited)
    # bắt đầu từ đỉnh gốc
    visited[s] = True
    q.put(s)

    # loang đường đi
    while not q.empty():
        u = q.get()                 # lấy đỉnh U ra khỏi queue để xét
        for v in graph[u]:          # xét các đỉnh V kề đỉnh U
            if not visited[v]:
                visited[v] = True   # đánh dấu đã thăm
                q.put(v)            # thêm vào queue các đỉnh kề khác (vòng while sau xét)
                path[v] = u         # đánh dấu đỉnh trước V là U


# tìm đường đi từ s->f dùng đề quy
def printPathRecursion(s, f):
    if s == f:
        print(f, end=' ')
    else:
        if path[f] == -1:
            print('No path')
        else:
            printPathRecursion(s, path[f])
            print(f, end=' ')


# tìm đường đi từ s -> f ko dùng đề quy
def printPath(s, f):
    b = []              # mảng kết quả
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print('No path')
        return
    # truy ngược lại
    while True:
        b.append(f)     # bắt đầu từ đỉnh f
        f = path[f]     # tiếp theo sẽ là đỉnh trước đỉnh f
        if f == s:      # đến cuối rồi
            b.append(s)
            break
    # in ngược lại do đang đi ngược từ f -> s
    for i in range(len(b)-1,-1,-1):
        print(b[i],end=' ')


if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)                  # đồ thị không hướng
        graph[v].append(u)

    s = 0
    f = 5
    BFS(s)
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
# output: 0 1 5



