# Cải tiến DSU

# vd có cấu trúc DSU như sau: a-b-c-root. Rõ ràng cả a, b, c đều có ptử đại diện là root, nếu truy vấn từ a sẽ bị quá dài
# => nối trực tiếp a, b, c vào root
# => cải tiến hàm find (path compression - càng đi chiều cao cây càng giảm)

# vd hàm union bth thì nối 2 tập hợp bất quy tắc. Giả sử có 2 tập hợp thì nếu thằng nào cao hơn làm gốc thì rank (thì khi tìm ptử đại diện cao nhất thì tốn cùng lắm là chiều cao thằng cao hơn)
# => cải tiến union by size: thằng nào lớn hơn thì làm gốc
# => by size là dựa vào kích thước dự đoán chiều cao cây, sao ta k lưu chiều cao cây luôn => union by rank

# khi đếm thành phần liên thông, ta chỉ cần check nếu i == parent[i] thì đó là 1 thành phần liên thông (nút đại diện cao nhất mới có parent là chính nó)

MAX = 20
parent = []
ranks = []

def makeSet():
    global parent, ranks
    parent = [i for i in range(MAX + 5)]        # parent[i] là đại diện cho i, ban đầu mỗi ptử đại diện chính nó
    ranks = [0 for i in range(MAX + 5)]         # ban đầu rank = 0 vì tập hợp chỉ có 1 ptử là chính nó


# path compression
def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])          # đệ quy khi parent[u] == u là đại diện cao nhất của nó
    return parent[u]


# union by rank
def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up == vp:                        # 2 tập hợp bằng nhau => chiều cao như nhau => bỏ qua
        return                          # phải return ở đây để ko ảnh hưởng ranks += 1 bị tăng ảo phía dưới
    if ranks[up] > ranks[vp]:           # cây nào cao hơn thì làm parent của cây còn lại
        parent[vp] = up
    elif ranks[up] < ranks[vp]:
        parent[up] = vp
    else:                               # 2 rank bằng nhau thì cho ai làm gốc cũng đc
        parent[up] = vp                 # chọn vp là cha
        ranks[vp] += 1                  # thì tăng rank cha lên 1 (1 đường nối từ thằng cha xuống thằng con, 2 vòng if trên ko tăng rank)


if __name__ == '__main__':
    Q = int(input())
    makeSet()
    for i in range(Q):
        u, v, q = map(int, input().split())
        if q == 1:
            unionSet(u, v)
        if q == 2:
            parentU = findSet(u)
            parentV = findSet(v)
            if parentU == parentV:
                print('YES')
            else:
                print('NO')
