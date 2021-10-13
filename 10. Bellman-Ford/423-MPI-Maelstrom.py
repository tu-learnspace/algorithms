"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=364

- để phát một tin nhắn từ 1 máy chủ tới tất cả n – 1 máy khác, ta phải tuần tự gửi tin nhắn đó n – 1 lần => mất thời gian và hiệu suất kém
- khi máy chủ đầu tiên đã gửi tin nhắn cho một máy khác, thì lúc này cả hai có thể tiếp tục gửi tin nhắn cho hai máy khác cùng một lúc. Sau đó sẽ có bốn máy có thể gửi, v.v… (khá giống cây nhị phân)
- mỗi đường truyền sẽ có chi phí khác nhau
- gói tin có thể đi theo một trong hai hướng với chi phí bằng nhau (đồ thị vô hướng)
- in thời gian giao tiếp tối thiểu cần thiết để phát sóng một tin nhắn từ nút đầu tiên đến tất cả các nút khác

- input là ma trận kề, nhưng chỉ có tam giác dưới, vì A(i, i) = 0 và A(i, j) = A(j, i)

IDEA:
- tìm thời gian nhỏ nhất từ đỉnh 1 đến tất cả các đỉnh còn lại
=> xài bellman
- ta có được thời gian nhỏ nhất từ đỉnh 1 đến đỉnh bất kỳ trong đồ thị => đáp án là thời gian lớn nhất trong tập thời gian đó
"""
INF = 1e9


def bellman(src):
    dist[src] = 0

    for _ in range(1, n):
        for source, target, weight in graph:
            if dist[source] + weight < dist[target]:
                dist[target] = dist[source] + weight


n = int(input())
dist = [INF] * (n + 1)
graph = []

for i in range(2, n + 1):                   # chuyển từ nửa dưới của ma trận kề thành danh sách cạnh => chạy từ 2 tới n (vì đường chéo A(i, i) = 0)
    line = input().split()

    for j in range(1, i):                    # chỉ là tam giác dưới của ma trận kề (từ 1 -> i-1)
        if line[j - 1] != 'x':               # j - 1 vì string bắt đầu từ index 0
            weight = int(line[j - 1])
            graph.append((i, j, weight))     # đồ thị 2 hướng: A(i, j) = A(j, i)
            graph.append((j, i, weight))

bellman(1)

totalTime = 0
for i in range(1, n + 1):                    # tìm thời gian lớn nhất giữa tập các thời gian nhỏ nhất
    if dist[i] > totalTime:
        totalTime = dist[i]

print(totalTime)