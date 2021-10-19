"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1524

- dùng DSU hợp mấy người có cùng tôn giáo
- đếm số phần tử đại diện cao nhất (i == parent[i])
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


tc = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    parent = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)

    for _ in range(m):
        i, j = map(int, input().split())
        union(i, j)

    res = 0
    for i in range(1, n + 1):
        if i == parent[i]:
            res += 1

    print('Case {}: {}'.format(tc, res))
    tc += 1

