"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1498

- game có các căn phòng, có căn phòng xuất phát & kết thúc
- mỗi căn phòng có 1 nguồn mana (-100 -> 100)
- người chơi có mana = 100 tại căn phòng bắt đầu rồi đi qua các căn phòng, mỗi lần đi qua thì + thêm lượng mana của căn phòng đó
- trò chơi end khi tới đc phòng kết thúc hoặc mana tụt xuống = 0
- người chơi có thể quay lại các phòng để thêm năng lượng
- tìm xem game đó có winnable hay hopeless

IDEA:
- cần tìm đường đi từ start tới end có tổng mana lớn nhất (để ko phải thua vì hết mana)
=> cần tìm chu trình dương (để tăng mana lên mức vô cực) => dùng bellman-ford
- tuy nhiên có thể đi xong chu trình dương mà ko tới end đc => duyệt BFS/DFS tại đỉnh coi có đường đi ko
- ta ko cần lưu trọng số trên cạnh vì thật sự trọng số chỉ ở đỉnh cuối chứ k phải cạnh
"""
from queue import Queue
INF = int(1e9)

def bfs(s, e):
    visited = [False] * (n + 1)
    q = Queue()
    q.put(s)
    visited[s] = True

    while not q.empty():
        top = q.get()
        for edge in graph:                     # vì graph hiện tại lưu là [(1,2), (2,3), (3,4), ...] khác với cách lưu trong bfs (graph = [[] for _ in range()] rồi graph[start].append(end)
            source, target = edge
            if source == top:                  # check convert danh sách cạnh (bellfordman) thành danh sách kề (bfs) đúng k
                if not visited[target]:
                    visited[target] = True
                    q.put(target)
                if target == e:
                    return True

    return False


def bellman(start, end):
    dist = [-INF] * (n + 1)
    dist[start] = 100

    for _ in range(n):
        for edge in graph:
            source, target = edge
            if dist[source] > 0 and dist[source] + energy[target] > dist[target]:   # đang ngc lại bellfordman, tìm dài nhất (tận dụng chu trình dương)
                dist[target] = dist[source] + energy[target]

    # kiểm tra lại coi dài hơn đc nữa ko
    for edge in graph:
        source, target = edge
        if dist[source] > 0 and dist[source] + energy[target] > dist[target] and bfs(source, end):       # vẫn có thể dài hơn và có đường đi đến căn phòng cuối cùng
            return 'winnable=='

    # hết mana trc khi tới căn phòng cuối, vẫn phải check ở đây vì có TH vẫn win mà ko cần chu trình dương
    if dist[end] <= 0:
        return 'hopeless'
    else:
        return 'winnable'


while True:
    graph = []
    energy = [0] * (100 + 5)

    n = int(input())
    if n == -1:
        break
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        energy[i] = line[0]
        m = line[1]

        index = 2
        for _ in range(m):
            graph.append((i, line[index]))
            index += 1

    print(bellman(1, n))
