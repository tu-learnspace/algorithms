"""
https://www.spoj.com/problems/MAKEMAZE/

- Mê cung hợp lệ là mê cung chỉ có 1 điểm vào và 1 điểm ra và có con đường nối 2 điểm đó
- Xác định mê cung là hợp lệ hay không hợp lệ

- Input:
    + dòng 1: số lượng testcase. Mỗi testcase bao gồm:
        + dòng 1: M-số hàng, N-số cột mê cung
        + các dòng còn lại miêu tả mê cung. với # là bước tường, . là khoảng cách
- Output: mỗi TH in ra mê cung là valid hay invalid

IDEA:
- tìm điểm đầu, điểm cuối (là những điểm ở 4 cạnh) => nhiều hơn 2 là false
- tìm đường đi từ điểm đầu. nếu đến cuối == điểm cuối đã tìm thì true, ngc lại false
"""
from queue import Queue


def checkBFS(maze, M, N, start, end):
    visited = [None] * M
    for i in range(M):
        visited[i] = [False] * N

    q = Queue()
    check = False
    q.put(start)

    while not q.empty():
        temp = q.get()

        # check was visited or out of range
        if temp[0] >= M or temp[0] < 0 or temp[1] >= N or temp[1] < 0:
            continue
        elif visited[temp[0]][temp[1]]:
            continue

        if temp == end:
            check = True
            break

        visited[temp[0]][temp[1]] = True

        # chỉ tiếp tục loang ra xung quanh nếu đang xét là điểm '.'. mấy điểm '#' thì đã bị pop rồi, ko quan tâm nữa
        if maze[temp[0]][temp[1]] == '.':
            q.put([temp[0] + 1, temp[1]])
            q.put([temp[0] - 1, temp[1]])
            q.put([temp[0], temp[1] + 1])
            q.put([temp[0], temp[1] - 1])
    return check


if __name__ == '__main__':

    testcase = int(input())
    for _ in range(testcase):
        # read input
        M, N = map(int, input().split())
        maze = [None] * M
        for i in range(M):
            maze[i] = list(input())

        # find start, end
        cnt = 0     # count số điểm đầu, cuối
        point = []  # chứa điểm đầu, cuối
        for i in range(M):
            for j in range(N):
                if (i == 0 or i == M - 1 or j == 0 or j == N - 1) and maze[i][j] == '.':
                    point.append([i, j])
                    cnt += 1

        if cnt != 2:
            print('invalid')
        else:
            start = point[0]
            end = point[1]
            if checkBFS(maze, M, N, start, end):
                print('valid')
            else:
                print('invalid')
