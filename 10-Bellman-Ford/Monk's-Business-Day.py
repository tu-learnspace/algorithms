"""
https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/monks-business-day/

- Có N món hàng (đánh số từ 1 -> N) đc buôn bán bởi M thương gia
- Mỗi thương gia được đặc trưng bởi i, j, C:
    thương gia muốn nhận món hàng i từ bạn thì phải đưa bạn món hàng j với C đồng
    nếu C âm nghĩa là bạn muốn có món j từ thương gia thì phải đổi bằng i và C đồng
- Ta bắt đầu từ món hàng 1
- Kiểm tra xem liệu có cách trao đổi nào mà có thể khiến ta trở nên giàu một cách vô hạn hay không

IDEA:
- mỗi giao dịch ta lưu thành đồ thị, với trọng số mỗi cạnh là số tiền ta nhận đc sau khi giao dịch
- giàu 1 cách vô hạn tức là có chu trình dương => đi qua nhiều lần thì số tiền cứ tăng
=> dùng bellman để phát hiện chu trình dương
"""
INF = 1e9


def bellman(src):
    dist[src] = 0

    for _ in range(n):
        for source, target, weight in graph:
            if dist[source] != -INF and dist[target] < dist[source] + weight:
                dist[target] = dist[source] + weight

    # check chu trình dương
    for source, target, weight in graph:
        if dist[source] != -INF and dist[target] < dist[source] + weight:
            return 'Yes'

    # nếu ko có chu trình dương thì chắc chắn ko thể nào giàu vô hạn
    return 'No'


tc = int(input())
for _ in range(tc):
    graph = []
    n, m = map(int, input().split())
    dist = [-INF] * (n + 1)
    for _ in range(m):
        i, j, c = map(int, input().split())
        graph.append((i, j, c))

    print(bellman(1))
