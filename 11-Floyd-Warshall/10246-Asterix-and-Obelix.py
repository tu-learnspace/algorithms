"""
https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1187

- tìm đường đi có chi phí ngắn nhất từ đỉnh tới đích. trong đó cộng thêm giá trị lớn nhất của bữa tiệc trên đường đi đó
- đề bài yêu cầu tính chi phí thấp nhất về nhà, tức là tổng chi phí
=> con đường ngắn nhất chưa chắc có chi phí tốt nhất vì còn tính thêm chi phí buổi tiệc vô => ko thể chạy 2 lần floyd riêng lẻ cho graph và max_fee đc
=> chạy floyd rồi cập nhật graph lẫn max_fee dựa trên đường đi của graph
- do có thêm tham số max_fee => có TH floyd 1 lần ko tối ưu (floyd quá tham lam) => chạy đến khi ko có sự thay đổi thì mới có đáp án tối ưu
"""
INF = int(1e9)


def floyd():
    improver = False
    for k in range(city):
        for i in range(city):
            if graph[i][k] == INF:
                continue
            for j in range(city):
                if graph[k][j] != INF and graph[i][j] + max_fee[i][j] > graph[i][k] + graph[k][j] + max(max_fee[i][k], max_fee[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    max_fee[i][j] = max(max_fee[i][k], max_fee[k][j])
                    improver = True
    return improver


tc = 1
while True:
    city, road, q = map(int, input().split())
    if city == road == q == 0:
        break

    max_fee = [[0 for _ in range(city)] for _ in range(city)]       # chứa phí tiệc max trên con đường u, v
    party_fee = list(map(int, input().split()))
    graph = [[INF for _ in range(city)] for _ in range(city)]
    for i in range(city):
        graph[i][i] = 0
        max_fee[i][i] = party_fee[i]

    for _ in range(road):
        c1, c2, d = map(int, input().split())
        graph[c1 - 1][c2 - 1] = d
        graph[c2 - 1][c1 - 1] = d
        max_fee[c1 - 1][c2 - 1] = max(party_fee[c1 - 1], party_fee[c2 - 1])
        max_fee[c2 - 1][c1 - 1] = max(party_fee[c1 - 1], party_fee[c2 - 1])

    still_improve = floyd()
    while still_improve:
        still_improve = floyd()


    print('Case #{}'.format(tc))
    for _ in range(q):
        c1, c2 = map(int, input().split())
        if graph[c1 - 1][c2 - 1] != INF:
            print(graph[c1 - 1][c2 - 1] + max_fee[c1 - 1][c2 - 1])
        else:
            print(-1)
    print()

    tc += 1
