"""
https://www.spoj.com/problems/KOZE/

- '.' là ô trống. '#' là hàng rào. 'k' là một con cừu. 'v' là một con sói.
- 2 ô được xem cùng một vùng, nếu như ta có thể đi sang mà ko cần đi qua hàng rào. ko đc đi xéo
- nếu như từ một ô, có thể đi hẳn ra khỏi ngoài khu vườn, ô đó sẽ tính là không thuộc vào vùng nào cả
- cừu ở ô ko thuộc bất kỳ vùng nào có thể chạy tứ phía => ko con nào bị chết
- trong 1 vùng, cừu > sói => sói die hết, cừu sống và ngc lại

- Input:
    + dòng 1: N-số hàng, M- số cột khu vường
    + mỗi dòng N tiếp theo chứ M kí tự đại diện khu vườn
- Output: in ra số cừu và sói sống sót

IDEA:
- duyệt bfs loang ra thành các khu vực. khu vực nào
- đánh dấu '#' là visited lúc đọc mảng luôn để khỏi xét tới
- loang ra từng khu vực => biết đc số cừu & sói trong khu vực đó => số con sống sót
- khu vực nào có phần tử thuộc 4 cạnh => ko bị rào => số cừu & sói giữ nguyên
"""
from queue import Queue
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(yard, visited, start, N, M):
    sheep = wolves = 0
    checkFence = False
    q = Queue()
    q.put(start)
    visited[start[0]][start[1]] = True

    while not q.empty():
        temp = q.get()

        if yard[temp[0]][temp[1]] == 'k':
            sheep += 1
        elif yard[temp[0]][temp[1]] == 'v':
            wolves += 1

        for i in range(4):
            next_x = temp[0] + dx[i]
            next_y = temp[1] + dy[i]

            if next_x in range(N) and next_y in range(M):
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.put([next_x, next_y])
                    # nếu là khu vực bị rào
                    if next_x == 0 or next_x == N - 1 or next_y == 0 or next_y == M - 1:
                        checkFence = True

    if not checkFence:
        if sheep > wolves:
            wolves = 0
        else:
            sheep = 0

    return [sheep, wolves]


if __name__ == '__main__':
    N, M = map(int, input().split())

    yard = [None] * N
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        yard[i] = list(input())
        for j in range(M):
            if yard[i][j] == '#':
                visited[i][j] = True

    sheep = wolves = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                start = [i, j]
                survial = BFS(yard, visited, start, N, M)
                sheep += survial[0]
                wolves += survial[1]

    print(sheep, wolves)
