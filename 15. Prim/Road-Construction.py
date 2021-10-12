"""
https://lightoj.com/problem/road-construction

- cho danh sách <thành phố> <chi phí>
- nếu chi phí = 0 => con đường vẫn đang đc thành phố sử dụng
- nểu chi phí != 0 => con đường cần đc sửa vs chi phí đó
- mọi thành phố phải có ít nhất 1 đường đi, có thể có nhiều đường đi giữa 2 tp
- tìm chi phí ít nhất để xây dựng lại tất cả các con đường, nếu k thì in impossible (nghĩa là ko liên thông)

IDEA:
- chi phí xây dựng lại tất cả các con đường nhỏ nhất => cây khung nhỏ nhất => prim
- cần check có liên thông không (để in impossible)
=> vì ban đầu khởi tạo dist = inf. nên sau khi chạy prim, nếu tại 1 nút (thành phố) nào đó dist vẫn = inf => impossible

"""
import heapq
INF = 1e9

def prim(src, n):
    dist = [INF for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = []

    heapq.heappush(pq, (0, src))
    dist[src] = 0
    totalCost = 0

    while len(pq) > 0:
        top = heapq.heappop(pq)

        if visited[top[1]]:
            continue
        visited[top[1]] = True

        totalCost += top[0]

        for neighbor in graph[top[1]]:
            if not visited[neighbor[1]] and neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = neighbor[0]
                heapq.heappush(pq, (neighbor[0], neighbor[1]))

    # check nếu tp ko liên thông
    for i in range(n):
        if dist[i] == INF:
            return 'Impossible'

    return totalCost



tc = int(input())
for i in range(tc):
    input()

    cities = dict()     # map city with id
    graph = []          # ban đầu k biết bao nhiêu tphố
    nextAvailableID = 0

    m = int(input())
    for _ in range(m):
        start, end, cost = input().split()

        if start in cities:
            u = cities[start]               # lấy city id dựa trên tên
        else:
            u = nextAvailableID             # nếu chưa có thì push vào dict vs id tiếp theo
            cities[start] = nextAvailableID
            nextAvailableID += 1            # tăng id cho tphố tiếp theo
            graph.append([])                # tăng graph size

        if end in cities:
            v = cities[end]
        else:
            v = nextAvailableID
            cities[end] = nextAvailableID
            nextAvailableID += 1
            graph.append([])

        cost = int(cost)
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    print('Case {}: {}'.format(i + 1, prim(0, nextAvailableID)))


