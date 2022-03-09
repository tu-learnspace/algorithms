"""
https://www.spoj.com/problems/CAM5/

- Có các nhóm người, cần chia sẻ tin tức cho họ
- Bạn của nhau thì sẽ truyền tin cho nhau
- Thay vì đi gặp từng người, ta chỉ gặp một vài người, để 1 vài người đó truyền tin đi cho người khác và so on
- Tìm số người cần gặp để truyền tin đến hết cho mọi người

- Input:
    + dòng 1: T-số lượng testcase. Với mỗi testcase:
        + dòng đầu tiên: N-số người
        + dòng tiếp theo: E-số quan hệ bạn bè (cạnh của đồ thị)
        + các dòng tiếp theo: a b-có quan hệ giữa a, b (a là bạn của b và ngc lại)
- Output: tương ứng với mỗi testcase, in ra số người tối thiểu cần gặp

IDEA:
- bạn bè thì truyền tin nhau => duyệt dfs từng người, những người liên quan tới người đó thì đánh dấu visited
- đáp án là số người chưa visited
"""
import sys
MAX = 10**5
sys.setrecursionlimit(MAX)


def DFS(s):
    visited[s] = True

    for u in graph[s]:
        if not visited[u]:
            visited[u] = True
            DFS(u)

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        graph = [[] for _ in range(MAX)]
        visited = [False for _ in range(MAX)]

        N = int(input())
        E = int(input())
        for _ in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        peer = 0
        for i in range(N):
            if not visited[i]:
                DFS(i)
                peer += 1

        print(peer)

