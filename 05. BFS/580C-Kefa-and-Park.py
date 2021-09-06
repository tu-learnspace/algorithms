"""
https://codeforces.com/problemset/problem/580/C

- Rooted tree có gốc là đỉnh 1
- Các node i có mèo sẽ được đánh dấu trong mảng Ai
- Các tập cạnh đã cho đảm bảo tạo thành cây có nghĩa
- Tìm con đường tới node lá (cuối cùng), sao cho đường đi ko vượt quá số mèo M cho trước

- Input:
    + dòng 1: N-số đỉnh của cây, M-số đỉnh liên tiếp có mèo có thể đi qua
    + dòng 2: mảng An-ptử Ai = 0 thì nút i ko có mèo, = 1 thì có mèo
    + N-1 dòng tiếp theo: thể hiện các cạnh nối đỉnh
- Output: số lượng là có thể tới mà đường đi đến ko quá M đỉnh liên tiếp có mèo

IDEA:
- duyệt đường đi bfs
- dùng một mảng cat để lưu số mèo đã đi qua (công dụng tương tự mảng dist):
    + vd có u -> v thì nếu tại v đó mèo => cat[v] = cat[u] + 1
    + ko có thì thôi (mặc định = 0, nghĩa là ko còn liên tiếp nữa nên đc reset thành 0)
"""
from queue import Queue
MAX = 100000 + 5

def BFS(graph, start, cat_path, visited, check_cats, M):
    count = 0
    q = Queue()
    q.put(start)
    cat_path[start] = check_cats[start - 1]
    visited[start] = True

    while not q.empty():
        u = q.get()

        # nếu là lá
        if len(graph[u]) == 1 and cat_path[u] < M + 1 and u != start:  # 2 cái sau cho TH chỉ có 2 nút thì ko xét tới else đc
            count += 1
        else:
            for v in graph[u]:
                if not visited[v]:
                    if check_cats[v - 1] == 1:
                        cat_path[v] = cat_path[u] + 1
                    visited[v] = True

                    # số mèo trên đường này chưa chạm mức limited thì mới push vô
                    if cat_path[v] < M + 1:
                        q.put(v)

    print(count)

if __name__ == '__main__':
    graph = [[] for _ in range(MAX)]
    visited = [False for _ in range(MAX)]
    cat_path = [0 for _ in range(MAX)]      # đếm số mèo trên con đường đó

    N, M = map(int, input().split())
    check_cats = list(map(int, input().split()))

    for i in range(N-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    start = 1
    BFS(graph, start, cat_path, visited, check_cats, M)