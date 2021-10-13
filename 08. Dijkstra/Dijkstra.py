# Dijkstra tìm đường đi ngắn nhất từ 1 đỉnh tới các đỉnh còn lại trên đồ thị ko âm
# Ý tưởng tham lam, duyệt theo đỉnh.
# Với mỗi đỉnh kể đỉnh đang xét, nếu như đường đi tới đỉnh đó thông qua đỉnh kề đó tốt hơn thì cập nhật
# Nhược điểm: vì quá tham lam nên sẽ có 1 số TH phải chạy nhiều lần mới đúng (vd bài 10246-Asterix-and-Obelix)

# Độ phức tạp: O(V^2) - xét theo đỉnh
#   - dùng heap: đpt O(ElogV)
#   - dùng cây nhị phân tìm kiếm: O(ElogV)

import heapq
MAX = 100
INF = int(1e9)  # dist ban đầu là vô cực

# thuật toán chính => cập nhật mảng dist là khoảng cách ngắn nhất từ s đến
def dijkstra(s):
    pq = []
    dist[s] = 0                             # đỉnh bắt đầu thì dist = 0
    heapq.heappush(pq, (0,s))

    while len(pq):
        top = heapq.heappop(pq)     # ptử bé nhất trong heap (vì đã lưu dạng tuple nên python so sánh dist rồi tới id)
        curr_dist = top[0]          # dist
        curr_id = top[1]            # id

        if curr_dist != dist[curr_id]:       # tránh TH nút cổ chai (vd đồ thị có 1 nút cổ chai, thì trong heap sẽ có rất nhiều phiên bản của nút đó)
            continue                         # => ta chỉ cần continue ở những phiên bản cũ/ko tối ưu (vì ko tối ưu nên mới chưa đc cập nhật vào dist)

        for neighbor in graph[curr_id]:      # neighbor[0]: chi phí để đi đến neigher từ curr_id
            if dist[neighbor[1]] > curr_dist + neighbor[0]:                 # đường đi tới neighbor cũ lớn hơn đường đi tới neighbor mới => đường đi mới tốt hơn (ở bước đầu tiên thì luôn đc thì dist ban đầu là vô cực)
                dist[neighbor[1]] = curr_dist + neighbor[0]                 # thì cập nhật lại đường đi
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))        # push (dist, id) mới vào
                path[neighbor[1]] = curr_id                                 # cập nhật path (tới đc neighbor_id thì đi qua curr_id)


# in đường đi từ s -> f
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
    n = int(input())

    graph = [[] for _ in range(n+5)]        # lưu đỉnh kề dưới dạng (đỉnh, chi phí đi)
    dist = [INF for _ in range(n+5)]        # chi phí đi tới đỉnh i
    path = [-1 for _ in range(n+5)]         # đỉnh trc (đường đi)

    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append((d[j], j))  # lưu node dưới dạng 1 tuple: (dist, id) => python tự so sánh dist rồi tới id

    s = 0
    dijkstra(s)
    ans = dist[4]
    print('Min path from', s, 'to 4:', ans)

    print('Full path: ')
    printPathRecursion(0, 4)

# input dưới dạng ma trận kề (adjacency matrix): 6 đỉnh
# 6
# 0 1 0 0 0 0
# 0 0 5 2 0 7
# 0 0 0 0 0 1
# 2 0 1 0 4 0
# 0 0 0 3 0 0
# 0 0 0 0 1 0
# => output: Min path from 0 to 4: 6
# full path
# 0 1 3 2 5 4

# dạng edge list: 6 đỉnh, 10 cạnh
# 6 10
# 0 1 1
# 1 2 5
# 1 3 2
# 1 5 7
# 2 5 1
# 3 0 2
# 3 2 1
# 3 4 4
# 4 3 3
# 5 4 1
