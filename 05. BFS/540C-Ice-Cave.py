"""
https://codeforces.com/problemset/problem/540/C

- Trò chơi đi qua các ô băng và rớt xuống dưới để qua màn tiếp
- Đi vào ô bị nứt sẽ rớt xuống dưới tại vị trí đó
- Đi vào một ô cứng, ô đó sẽ thành ô nứt
- Cho điểm xuất phát (chắc chắn là 'X') và điểm kết thúc. hỏi có thể rớt xuống màn tiếp theo không

- Input:
    + dòng 1: n-số hàng, m-số cột của bàn cờ băng
    + n dòng tiếp theo hiển thị bàn cờ băng. '.' là ô cứng. 'X' là ô nứt
    + dòng tiếp theo: r1 c1-điểm xuất phát
    + dòng tiếp theo: r2 c2- vị trí ô phải rớt xuống
- Output: YES hoặc NO

IDEA:
- nếu điểm cuối là ô nứt thì ok qua màn, nếu là ô cứng thì phải đi qua 2 lần (để thành ô nứt)
- nghĩa là điểm cuối phải được visited rồi (đã có thể đến điểm cuối từ điểm khác)
    + check điểm cuối đã visited chưa khi loang => khi loang tới mà đã visited (đã nứt) thì YES (nứt rồi thì đi tới là rớt xuống)
- cho điểm 'X' là visited => như v sẽ ko duyệt bfs trúng ô nứt
"""
from queue import Queue
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(icecave, visited, start, end, n, m):
    q = Queue()
    q.put(start)

    while not q.empty():
        temp = q.get()
        for i in range(4):
            next_x = temp[0] + dx[i]
            next_y = temp[1] + dy[i]
            if next_x in range(n) and next_y in range(m):
                if next_x == end[0] and next_y == end[1] and visited[next_x][next_y]:
                    return True
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    q.put([next_x, next_y])
    return False


if __name__ == '__main__':
    n, m = map(int, input().split())

    icecave = [None] * n
    visited = [[False for _ in range(m)] for _ in range(n)]
    for i in range(n):
        icecave[i] = list(input())
        for j in range(m):
            if icecave[i][j] == 'X':
                visited[i][j] = True

    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    start = [r1 - 1, c1 - 1]
    end = [r2 - 1, c2 - 1]

    if BFS(icecave, visited, start, end, n, m):
        print('YES')
    else:
        print('NO')


