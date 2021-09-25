INF = int(1e9)
MAX = 105
dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]
graph = []

def bellmanford(s):
    dist[s] = 0                     # nơi bắt đầu là đứng tại chỗ

    for _ in range(1, V):           # duyệt qua các đỉnh (lặp để tìm V-1 cạnh, vì có V đỉnh thì tối đa là V-1 cạnh)
        improver = False            # cải tiến hơn = cách check xem nếu lần duyệt qua tất cả các cạnh lần đó mà ko có cạnh nào cải tiến => đã tối ưu rồi
        for j in range(E):  # mỗi lần như vậy duyệt qua tất cả các cạnh
            source = graph[j][0]
            target = graph[j][1]
            weight = graph[j][2]

            # nếu chưa có đường đi tới source và đường đi mới tốt hơn đường đi cũ
            if dist[source] != INF and dist[source] + weight < dist[target]:
                dist[target] = dist[source] + weight
                path[target] = source
                improver = True         # có cải tiến => vẫn có thể còn cải tiến đc tiếp
        if not improver:                # nguyên vòng lặp con mà ko cải tiến đc gì => đã tối ưu => break luôn ko cần xét nữa
            break

    # sau khi đã duyệt xong vòng for trên => tìm đc tối đa là V-1 cạnh cho đường đi ngắn nhất
    # nếu vẫn còn cải tiến đc => có chu trình âm
    for i in range(E):  # duyệt lại toàn đồ thị 1 lần cuối để xem
        source = graph[i][0]
        target = graph[i][1]
        weight = graph[i][2]
        if dist[source] != INF and dist[source] + weight < dist[target]:    # nếu vẫn còn cải tiến đc
            return False    # nghĩa là có chu trình âm (vì thật vô lý nếu ta có thể cải tiến đường đi ngắn nhất)
    return True


def print_path(s, e):
    if s == e:
        print(s, end=' -> ')
    else:
        if path[e] == -1:
            print('No path')
        else:
            print_path(s, path[e])
            print(e, end=' -> ')


if __name__ == '__main__':
    V, E = map(int, input().split())
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph.append((u, v, w))

    start, end = 0, 4
    res = bellmanford(start)

    if not res:
        print('Graph contains negative weight cycle')
    else:
        print_path(start, end)
        print('')
        print('Cost:', dist[end])

# input:
# 6 10
# 0 1 1
# 1 2 5
# 1 3 -2
# 1 5 7
# 2 5 -1
# 3 0 2
# 3 2 -1
# 3 4 4
# 4 3 3
# 5 4 1
# output:
# 0 -> 1 -> 3 -> 2 -> 5 -> 4 ->
# Cost: -2