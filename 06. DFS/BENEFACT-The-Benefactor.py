"""
https://www.spoj.com/problems/BENEFACT/

- cho danh sách của các đoạn đường.
- cho biết giữa hai điểm chỉ có một đoạn đường duy nhất.
- tìm ra khoảng cách lớn nhất giữa hai điểm trong thành phố.

- input:
    + dòng đầu: số testcase, mỗi testcase có:
        - dòng đầu: số địa điểm trong thành phố
        - mỗi dòng tiếp theo là con đường: a b l - a,b: con đường a->b, l: độ dài con đường đó
- output: độ dài lớn nhất của con đường trong thành phố

IDEA:
- đồ thị có trọng số => graph lưu thêm trọng số
- giữa 2 đỉnh chỉ có 1 cạnh => đồ thị dạng cây
- đường đi lớn nhất chắc chắn nối giữa 2 node lá trong cây => tìm đường nối 2 node lá trong cây
=> đầu tiên duyệt dfs từ 1 tìm node lá bắt đầu (chắc chắn tìm đc node lá)
- sau đó từ node lá đó tiếp tục duyệt dfs qua các node lá khác => cập nhật đc max

- bài này xài cách đệ quy bị TLE
"""
def dfs(src):
    global leaf, max_dist
    s = [src]
    dist[src] = 0

    while len(s) > 0:
        u = s.pop()
        for b, l in graph[u]:
            if dist[b] == -1:
                dist[b] = dist[u] + l
                max_dist = max(max_dist, dist[b])
                s.append(b)

    leaf = dist.index(max(dist))    # node lá phải là index của phần từ lớn nhất trong dist hiện tại


if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = V - 1   # vì đây là đồ thị cây
        graph = [[] for _ in range(V+1)]
        dist = [-1] * (V + 1)
        for i in range(E):
            a, b, l = map(int, input().split())
            graph[a].append((b, l))
            graph[b].append((a, l))

        max_dist = leaf = 0  # leaf đánh số từ 1 -> V

        # find leaf
        dfs(1)
        # dfs from that leaf
        dist = [-1] * (V + 1)
        dfs(leaf)

        print(max_dist)

# cách đệ quy
# import sys
# sys.setrecursionlimit(10**5 + 5)
#
# def dfs(src):
#     global leaf, max_dist
#
#     for b, l in graph[src]:
#         if dist[b] == -1:
#             dist[b] = dist[src] + l
#             max_dist = max(max_dist, dist[b])
#             dfs(b)
#
#     leaf = dist.index(max(dist))    # node lá phải là index của phần từ lớn nhất trong dist hiện tại
#
#
# if __name__ == '__main__':
#     tc = int(input())
#     for _ in range(tc):
#         V = int(input())
#         E = V - 1   # vì đây là đồ thị cây
#         graph = [[] for _ in range(V+1)]
#         dist = [-1] * (V + 1)
#         for i in range(E):
#             a, b, l = map(int, input().split())
#             graph[a].append((b, l))
#             graph[b].append((a, l))
#
#         max_dist = leaf = 0  # leaf đánh số từ 1 -> V
#
#         # find leaf
#         dist[1] = 0
#         dfs(1)
#
#         # dfs from leaf
#         dist = [-1] * (V + 1)
#         dist[leaf] = 0
#         dfs(leaf)
#
#         print(max_dist)
