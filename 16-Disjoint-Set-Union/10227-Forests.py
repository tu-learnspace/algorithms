"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1168

- P người, T cây trong khu rừng
- mỗi người sẽ nghe đc 1 số cây
- khi nghe tiếng cây đổ, mn sẽ bàn luận do cây nào gây ra
- có nhiều luồng ý kiến khác nhau (những người nghe các cây giống nhau sẽ có ý kiến giống nhau)
- hãy đếm số luồng ý kiến

IDEA:
- xem mỗi người là 1 đỉnh đồ thị
- mỗi người sẽ có set lưu các cây mình nghe đc
- 2 người có set giống nhau thì union 2 người đó lại
- cuối cùng đếm xem có bao nhiêu tập hợp (giống như đếm bao nhiêu tp liên thông => chỉ cần đếm ptử đại diện)
"""


def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return
    if ranks[pu] > ranks[pv]:
        parent[pv] = pu
    elif ranks[pv] > ranks[pu]:
        parent[pu] = pv
    else:
        parent[pu] = pv
        ranks[pv] += 1


tc = int(input())
input()
for _ in range(tc):
    p, t = map(int, input().split())
    parent = [i for i in range(p + 1)]
    ranks = [0] * (p + 1)
    tree = [set() for i in range(p + 1)]       # lưu các cây mà người i nghe đc, xài set thay vì xài mảng vì ta cần so sánh phần tử 2 set có giống nhau chứ k so sánh thứ tự

    line = input()
    while line != '':
        i, j = map(int, line.split())
        tree[i].add(j)

        try:
            line = input()
        except EOFError:
            break

    # xét các cặp người, cặp nào cùng nghe set cây giống nhau thì union lại
    for u in range(1, p + 1):
        for v in range(u + 1, p + 1):
            if tree[u] == tree[v]:
                union(u, v)

    res = 0
    for i in range(1, p + 1):
        if i == parent[i]:
            res += 1

    print(res)
    print('')

