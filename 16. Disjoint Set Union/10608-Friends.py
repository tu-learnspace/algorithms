"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1549

- Nếu A và B là bạn bè, B và C cũng là bạn bè => A và C sẽ thành bạn bè
- Cho n người dân và m số cặp người đc cho là bạn của nhau
- Tìm số lượng người trong nhóm bạn bè có nhiều người nhất trong thị trấn

IDEA:
- xem mỗi người là 1 node, quan hệ giữa 2 ng là 1 cạnh
- nếu theo quy tắc bắc cầu A-B-C, ta lại có thêm 1 cạnh nối nữa
=> nối xong sẽ ra đc 1 nhóm người
=> dùng union để nối
- dùng 1 mảng num để chứa thông tin có bao nhiêu đỉnh có đỉnh đó làm đại diện (nghĩa là số bạn chung, vd A-B-C thì mảng num là 2,3,2 -> B là parent có num cao nhất)

- bài này giống bài Prayatna ở lecture 6: DFS => vẫn có thể xài dfs duyệt
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
        num[pu] += num[pv]                      # số con của u += số con của v
    elif ranks[pv] > ranks[pu]:
        parent[pu] = pv
        num[pv] += num[pu]
    else:
        parent[pu] = pv
        ranks[pv] += 1
        num[pv] += num[pu]


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    ranks = [0] * (n + 1)
    num = [1] * (n + 1)                         # kích thước mỗi tập hợp nhận node i làm gốc, ban đầu chỉ = 1 là chính mỗi node đó
    for _ in range(m):
        u, v = map(int, input().split())
        union(u, v)

    ans = -1
    for i in range(1, n + 1):
        if i == parent[i]:                      # i là parent chính nó => i là đại diện cao nhất
            ans = max(ans, num[i])
    print(ans)

