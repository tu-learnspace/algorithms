# So với việc tìm đường đi ngắn nhất từ 1 đỉnh tới các đỉnh còn lại, dùng Bellman-Ford (duyệt cạnh, đồ thị âm) và Dijkstra (duyệt đỉnh, đồ thị ko âm)
# Thì Floyd-Warshall tìm đường đi ngắn nhất giữa TẤT CẢ các cặp đỉnh, đồ thị âm dương đề đc (đương nhiên có chu trình âm thì fail, vì chu trình âm làm gì đường đi ngắn nhất)
# Dùng ý tưởng quy hoạch động, lưu tất cả kết quả có được => lưu dạng ma trận
# Với mỗi cặp đỉnh u-v (2 vòng lặp), ta chèn vào 1 đỉnh trung gian K nào đó xem nó có tốt hơn ko (vòng lặp bên ngoài), nghĩa là từ u-k rồi k-v tốt hơn u-v
# => tổng cộng 3 vòng lặp

# Độ phức tạp: O(V^3)

# lưu graph dạng ma trận kề. graph có thể sử dụng như dist luôn
# ban đầu khởi tạo dist = graph. dist[i][j]: đường đi từ i -> j
# path[u][v]: đỉnh liền trc v trong đường đi từ u tới v => cập nhật path[i][j] = path[k][j]
# nếu có cạnh nối u -> v thì khởi tạo path[u][v] = u (ban đầu chỉ có 1 đường trực tiếp từ u -> v)
# ý tưởng là đường đi từ u -> v, thì ta thử kiếm điểm k sao cho u-k và k-v tối ưu hơn
INF = int(1e9)


# print a specific path
def print_path(s, f):
    if s == f:
        print(f, end='-')
    else:
        if path[s][f] == -1:
            print('No path', end='')
        else:
            print_path(s, path[s][f])
            print(f, end='-')


# print all solution
def print_solution():
    for i in range(V):
        for j in range(V):
            if i != j:
                print('Path {}->{}: '.format(i, j), end='')
                print_path(i, j)
                print()

                if path[i][j] != -1:
                    print('Total length: {}'.format(dist[i][j]))


def floydwarshall():
    # khởi tạo dist và path
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]            # khởi tạo dist = graph
            if graph[i][j] != INF and i != j:   # nếu có đường
                path[i][j] = i                  # đỉnh trc j trong i -> j ban đầu là i
            else:
                path[i][j] = -1                 # ko có đường

    # thuật toán chính
    for k in range(V):                  # với mỗi đỉnh k muốn chèn vô
        for i in range(V):              # xét ma trận kề (2 vòng loop)
            if dist[i][k] == INF:       # nếu ko có đường đi tới k thì xét làm gì nữa (đường đi từ i->k là vô cực)
                continue
            for j in range(V):
                if dist[k][j] != INF and dist[i][j] > dist[i][k] + dist[k][j]:  # có đường đi từ k tới j và nó tốt hơn
                    dist[i][j] = dist[i][k] + dist[k][j]    # cập nhật độ dài
                    path[i][j] = path[k][j]                 # cho k vào là 1 đỉnh mới giữa i và j

    # kiểm tra xem có chu trình âm tại điểm i hay ko
    for i in range(V):
        if dist[i][i] < 0:      # nếu có chu trình âm thì dist mới âm (vì nếu ko thì dist ko thể nào âm đc)
            return False
    return True


if __name__ == '__main__':
    V = int(input())    # số đỉnh
    # khởi tạo 3 cái y chang nhau
    graph = [[None for _ in range(V)] for _ in range(V)]
    dist = [[None for _ in range(V)] for _ in range(V)]
    path = [[None for _ in range(V)] for _ in range(V)]

    # nhập graph  dưới dạng ma trận kề
    for i in range(V):
        line = list(map(int, input().split()))
        for j in range(V):
            if line[j] == 0 and i != j:  # nếu là 0 và ko phải đường chéo (đang quy định nhập 0 là ko có cạnh nối)
                graph[i][j] = INF
            else:
                graph[i][j] = line[j]

    if floydwarshall():
        #print_solution()
        print_path(0, 4)
        print()
        print('Chi phi:', dist[0][4])
    else:
        print('Graph contains negative weight cycle')


# input ma trận kề, giả sử 0 là ko có cạnh nối:
# 6
# 0 1 0 0 0 0
# 0 0 5 -2 0 7
# 0 0 0 0 0 -1
# 2 0 -1 0 4 0
# 0 0 0 3 0 0
# 0 0 0 0 1 0

# output đường đi từ 0 -> 4:
# 0-1-3-2-5-4-
# Chi phi: -2

