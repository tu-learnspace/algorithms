"""
https://www.spoj.com/problems/MICEMAZE/

- có mê cung có các nút, chi phí giữa 2 nút xem như là thời gian di chuyển giữa 2 nút (chi phí chiều đi và chiều về có thể khác nhau)
- có 1 nút là nút đích để thoát khỏi mê cung
- cho mỗi chú chuột xuẩt phát ở mỗi nút, các chú chuột biết tìm đường đi ngắn nhất
- bộ đếm thời gian bắt đầu, hỏi có bao nhiêu con chuột thoát khỏi đc mê cung

- input
    + dòng 1: N-số ô trong mê cung
    + dòng 2: E-ô đích để thoát khỏi mê cung
    + dòng 3: T-thời gian giới hạn
    + dòng 4: M-số đường đi trong mê cung
    + M dòng tiếp theo thể hiện đường đi mê cung: a b w-đường đi từ a đến b có chi phí w
- ouput: số chuột thoát đc

IDEA:
- mỗi con chuột xuất phát từ các ô rồi tới nút E
=> thay vì xét đường đi ngắn nhất từ mỗi ô tới E thì xét đường đi ngắn nhất từ E tới các ô còn lại
- nhưng như vậy sẽ sai đường đi (vì đường đi và đường về cost có thể khác nhau)
=> cần đảo chiều đường đi lúc input
"""
import heapq
INF = int(1e9)
MAX = 10**5

def dijkstra(s):
    pq = []
    dist[s] = 0
    heapq.heappush(pq, (0, s))

    while len(pq):
        top = heapq.heappop(pq)
        curr_dist = top[0]
        curr_id = top[1]

        if curr_dist != dist[curr_id]:
            continue

        for neighbor in graph[curr_id]:
            if curr_dist + neighbor[0] < dist[neighbor[1]]:
                dist[neighbor[1]] = curr_dist + neighbor[0]
                heapq.heappush(pq, (dist[neighbor[1]], neighbor[1]))


n = int(input())
end = int(input())
time = int(input())
edges = int(input())

graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]

for _ in range(edges):
    a, b, w = map(int, input().split())
    graph[b].append((w, a))                 # reverse direction

dijkstra(end)

cnt = 0
for i in range(1, n+1):
    if dist[i] <= time:
        cnt += 1

print(cnt)
