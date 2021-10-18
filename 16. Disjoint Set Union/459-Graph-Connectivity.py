"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=400

- xét đồ thị G gồm các đỉnh và các kết nối
- G đc gọi là liên thông nếu tồn tại 1 đường đi trực tiếp hoặc qua các cạnh giữa 2 đỉnh bất kì
- liên thông cực đại là ko có đỉnh và cạnh trong đồ thị gốc có thể đc thêm vào vào đồ thị con mà vẫn giữ cho nó đc liên thông
- xác định số đồ thị con liên thông cực đại

IDEA:
- đây là bài toán đếm thành phần liên thông cơ bản => có thể dùng dfs/bfs đã học => tuy nhiên dùng DSU sẽ gọn hơn
- với mỗi cạnh thì union mỗi đỉnh. nên chuyển đổi đại diện node từ chữ cái => stt để dễ dàng hơn
- ban đầu có n thành phần liên thông (mỗi node là 1 thành phần liên thông)
- union các cạnh lại
=> với mỗi lần union thành công giảm tp liên thông đi 1 (do hợp đc 2 cái thành 1 thành phần liên thông)
"""


def find(u):
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu == pv:
        return False
    if ranks[pu] > ranks[pv]:
        parent[pv] = pu
    elif ranks[pv] > ranks[pu]:
        parent[pu] = pv
    else:
        parent[pu] = pv
        ranks[pv] += 1
    return True


tc = int(input())
input()
for _ in range(tc):
    C = input()                     # kí tự đại diện đỉnh lớn nhất trong đồ thị
    n = ord(C) - ord('A') + 1       # => tìm đc số đỉnh tối đa trong đồ thị

    parent = [i for i in range(n)]
    ranks = [0] * n
    ans = n

    line = input()
    while line != '':
        u = ord(line[0]) - ord('A')
        v = ord(line[1]) - ord('A')

        if union(u, v):
            ans -= 1

        try:
            line = input()
        except EOFError:
            break

    print(ans)
    print('')
