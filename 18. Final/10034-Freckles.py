"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=975

- cho các điểm
- tìm tổng các cạnh sao cho các cạnh:
    đi qua tất cả các điểm
    tổng trên là nhỏ nhất

IDEA:
- với mỗi 2 điểm => có danh sách các cạnh riêng biệt
- cần tìm sao cho tổng các cạnh là nhỏ nhất
=> sort danh sách cạnh tăng dần

- dùng DSU
- xét mỗi cạnh ta đc 2 điểm riêng biệt:
    + nếu 2 điểm ko thuộc cùng thành phần liên thông (tức là chưa có cạnh nào đi qua 2 điểm đó) => union nó lại thành 1 thành phần liên thông, rồi + độ dài cạnh vào res
    + đã thuộc 1 thành phần liên thông thì bỏ qua
(vì đã sort danh sách cạnh tăng dần theo độ dài => chắc chắn đc tổng là nhỏ nhất)

- để tiện union thì ta chỉ cần định danh mỗi điểm theo stt (vd điểm thứ 1, điểm thứ 2, v.v)
"""
import math


class Edge:
    def __init__(self, x, y, dist):     # x, y là stt 2 điểm nối thành cạnh có độ dài dist
        self.x = x
        self.y = y
        self.dist = dist

    def __lt__(self, other):
        return self.dist > other.dist


def calDist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return
    parent[pu] = pv


tc = int(input())
for _ in range(tc):
    input()
    n = int(input())

    points = []

    # read all points
    for _ in range(n):
        x, y = map(float, input().split())
        points.append((x, y))

    # tính edges tử điểm thứ i & điểm thứ j
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            e = Edge(i, j, calDist(points[i][0], points[i][1], points[j][0], points[j][1]))
            edges.append(e)

    # sort edges
    edges.sort(reverse=True)

    parent = [i for i in range(n)]
    res = 0
    for e in edges:
        if find(e.x) != find(e.y):
            res += e.dist
            union(e.x, e.y)

    print('{:.2f}'.format(round(res, 2)))

    if tc != 1:
        print('')
