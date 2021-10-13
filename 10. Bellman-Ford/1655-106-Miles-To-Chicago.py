"""
https://www.urionlinejudge.com.br/judge/en/problems/view/1655

- tìm đường trốn khỏi Police sao cho đường đó an toàn nhất (khả năng an toàn cao nhất)
- mỗi con đường có dạng a, b, p: đường từ a-b (2 chiều) có tỉ lệ p mà đi qua vẫn an toàn

IDEA:
- xác suất khi đi qua mỗi con đường là nhân cho xác suất con đường trước
- cần tìm tuyến đường có tích probs lớn nhất với start tại đỉnh 1 và end tại đỉnh n
=> chạy bellman
- khi chạy bellman thì nhớ update cả 2 hướng (vì là đồ thị 2 chiều)
"""

def bellman(s):
    probs[s] = 1.0

    for _ in range(1, n - 1):
        for source, target, weight in graph:
            if probs[source] * weight > probs[target]:
                probs[target] = probs[source] * weight

            if probs[target] * weight > probs[source]:      # đồ thị vô hướng (2 chiều) nên làm 2 lần
                probs[source] = probs[target] * weight


while True:
    line = list(map(int, input().split()))
    if len(line) == 1:
        break

    n, m = line[0], line[1]
    graph = []
    for _ in range(m):
        a, b, p = map(int, input().split())
        graph.append((a, b, p / 100))

    probs = [-1.0] * (n + 1)            # xác suất tại mỗi đỉnh
    bellman(1)

    # dist tại đỉnh cuối
    print("{:.6f} percent".format(probs[n] * 100))
