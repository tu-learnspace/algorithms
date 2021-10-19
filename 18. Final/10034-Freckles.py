"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=975

- cho các điểm
- tìm các cạnh nối các điểm (có thể ko cần liền nhau) sao cho đi qua tất cả các điểm & tổng là nhỏ nhất

IDEA:
- có 2 điểm => danh sách các cạnh. tuy nhiên ko cần tính tổng tất cả các cạnh (chỉ cần đi qua điểm đó 1 lần là đc)
=> sort danh sách cạnh tăng dần
- dùng DSU
- mỗi 2 điểm đọc vào union nó lại:
    union thành công thì + cạnh nối 2 điểm đó vào res (vì đã sort nên chắc chắn bé nhất)
"""
import math

class Edge:
    def __init__(self, x, y, dist):
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
