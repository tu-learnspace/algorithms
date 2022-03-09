# Disjoint Set Union: Disjoint-Set, Union-Find
# ctdl dùng để phân nhóm, gom nhóm dữ liệu

# thao tác: thêm, xoá, sửa có ĐPT O(N)
# Với DSU, ta thao tác trực tiếp các ptử (vì nó còn lkết vs parent) => thao tác trên parent của chúng

# Bài toán:
# - đồ thị vô hướng N đỉnh (đánh số từ 1 tới N).
# - ở trạng thái ban đầu, các đỉnh k có cạnh nối.
# - để nối các đỉnh trong đồ thị thì cần các truy vấn:
#     u v 1: Union(u, v) nối đỉnh u và v
#     u v 2: Find(u), Find(v) kiểm tra liệu 2 đỉnh u, v có kết nối (cùng thuộc 1 tphần liên thông) hay k

# => có thể xài bfs/dfs nhưng đồ thị thay đổi liên tục => bfs/dfs nhiều lần & tốn ĐPT O(V+E)
# => thử xài DSU xem sao?
# DSU có ĐPT là O(H) - H: chiều cao cây, nhưng sẽ là O(N) trong TH cây suy biến (cứ leo thẳng 1 đường)
# => ko tối ưu hơn bfs/dfs
# => cần cải tiến hàm find (path compression - càng đi chiều cao cây càng giảm) và union (by rank)


MAX = 20
parent = []         # parent[i] là đại diện cho i trong DSU
                    # ban đầu là cây rời rạc => mỗi nút sẽ tự đại diện chính nó


# tạo tập hợp
def makeSet():
    global parent
    parent = [i for i in range(MAX + 5)]        # ban đầu mỗi node là đại diện của chính nó


# tìm ptử đại diện của tập hợp chứa u
def findSet(u):
    while u != parent[u]:       # từ u nhảy dần dần lên parent cao nhất
        u = parent[u]           # nhảy đến khi nào k nhảy đc nữa (nó là parent của chính nó)
    return u


# hợp tập chứa u và tập chứa v
def unionSet(u, v):
    up = findSet(u)     # tìm parent u
    vp = findSet(v)     # tìm parent u
    parent[up] = vp     # gán parent[vp] = up cũng đc


if __name__ == '__main__':
    Q = int(input())
    makeSet()
    for i in range(Q):
        u, v, q = map(int, input().split())     # đọc truy vấn loại 1 hay 2
        if q == 1:
            unionSet(u, v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV:              # cùng parent => cùng thành phần liên thông
                print('YES')
            else:
                print('NO')
