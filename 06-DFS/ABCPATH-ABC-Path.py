"""
https://www.spoj.com/problems/ABCPATH/

- cho một lưới hình chữ nhật chứa các kí tự Latin in hoa.
- tìm đường đi dài nhất, xuất phát từ 'A', đi qua các ô liền kề (theo hướng dọc, ngang và chéo), thỏa mãn chuỗi kí tự tạo thành từ đường đi là các kí tự liên tiếp trên bảng chữ cái.

IDEA:
- duyệt qua cả mảng, ô nào là 'A' thì duyệt dfs từ ô đó (A->B->C->...) lưu lại giá trị rồi cập nhật max
"""
import sys
sys.setrecursionlimit(10**5 +5)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(i, j, maze, dist, H, W):
    count = 0
    for t in range(8):
        r = i + dx[t]
        c = j + dy[t]
        if r in range(H) and c in range(W) and ord(maze[r][c]) == ord(maze[i][j]) + 1:
            res = dfs(r, c, maze, dist, H, W)
            count = max(count, res)     # vì có thể có nhiều hướng đi khi dfs từ 1 điểm => lấy cái max

    dist[i][j] = count + 1
    return dist[i][j]


if __name__ == '__main__':
    testcase = 0
    while 1:
        testcase += 1
        H, W = map(int, input().split())
        if H == 0 and W == 0:
            break

        maze = [None] * H
        dist = [[0] * W for _ in range(H)]
        for i in range(H):
            maze[i] = list(input())

        size = 0
        for i in range(H):
            for j in range(W):
                if maze[i][j] == 'A':
                    res = dfs(i, j, maze, dist, H, W)
                    size = max(res, size)

        print('Case ' + str(testcase) + ': ' + str(size))


