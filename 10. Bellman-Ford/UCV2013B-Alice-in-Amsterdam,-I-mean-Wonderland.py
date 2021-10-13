"""
https://www.spoj.com/problems/UCV2013B/

- giữa những di tích trong thành phố, con đường nối giữa chúng có thể là một số âm
- các di tích có thể tự nối chính nó
- khoảng cách giữa 2 di tích khác nhau = 0 nghĩa là không có đường nối trực tiếp giữa 2 di tích đó
- có thể có chu trình dương & chu trình âm

IDEA:
- chu trình dương thì bỏ qua ko cần quan tâm đến
- giữa 2 đỉnh u-v có 3 TH xảy ra:
    tồn tại chu tình âm trên đường từ u -> v
    ko có đường đi
    từ u -> v đi đc &  có đường đi ngắn nhất (ko có chu trình âm)
=> dùng bellman để kiểm tra
- có nhiều truy vấn u-v. thay vì mỗi truy vấn chạy bellman thì chạy bellman 1 lần cho tất cả các đỉnh rồi lưu kết quả vào mảng 2 chiều dist
- vì các đỉnh phía sau chu trình âm sẽ bị ảnh hưởng nên gán dist nó = -INF (ko thể tới đc do có chu trình âm chặn đường)
"""
INF = 1e9

def bellman(src):
    dist[src][src] = 0      # đứng tại chính nó

    for i in range(1, n):
        for source, target, weight in graph:
            if dist[source] != INF and dist[target] > dist[source] + weight:
                dist[target] = dist[source] + weight

    



tc = 1
while True:
    n = int(input())
    if n == 0:
        break


    graph = []
    dist = [[INF] * n for _ in range(n)]        # lưu dist là mảng 2 chiều để sử dụng lại đc cho nhiều truy vấn
    monuments = []                              # lưu tên di tích

    for i in range(n):
        name, *weights = input().split()         # vd n=3 thì input theo dạng: name weight1 weight2 weight3 (tên_thành_phố cost_tới_tp_0 cost_tới_tp_1 cost_tới_tp_2)
        monuments.append(name)

        for j in range(n):
            w = int(weights[j])
            if i == j and w >= 0:                # nếu tại di tích đó có khuyên lại chính nó (chu trình dương) thì cũng ko có ý nghĩa => cho w = 0 luôn
                w = 0
            if i != j and w == 0:                # w = 0 nghĩa là ko có đường nối giữa 2 di tích
                continue
            graph.append((i, j, w))

    # bellman tất cả các đỉnh
    for i in range(n):
        bellman(i)