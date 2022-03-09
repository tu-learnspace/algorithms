"""
https://codeforces.com/problemset/problem/723/D?locale=en

- '.' biểu thị ô nước, '*' là ô đất
- cho mảnh đất berland. cần tìm số ô nước ít nhất cần lấp lại sao cho thỏa số hồ còn lại
- chỉ lấp hồ (là những ô nước đc bao bọc trong đất liền)

- Input:
    + dòng 1: n,m-kích thước mảnh đất k-số hồ mong muốn còn lại sau khi lấp
    + n dòng tiếp theo: hiển thị mảnh đất
- Output:
    + dòng 1: in số ô ít nhất càn lấp
    + n dòng tiếp theo: hiển thị mảnh đất sau khi lấp hồ

IDEA:
- tạo stuct lưu thông tin hồ (ô bắt đầu, size hồ)
- duyệt dfs/bfs toàn vùng đất, lưu thông tin vào mảng struct hồ, sau đó sort tăng dần theo size
- số hồ phải lấp = tổng số hồ - số hồ mong muốn bị lấp
=> dựa vào mảng hồ đã sort mà chọn hồ phải lấp
=> duyệt lại bfs cho các hồ phải lấp => đánh dấu lại ô để lấp
"""
MAX = 10**5
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

class Lake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

def dfs_fill(src):
    s = []
    visited[src[0]][src[1]] = False
    s.append(src)

    while len(s) > 0:
        temp = s.pop()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if x in range(n) and y in range(m):
                if visited[x][y] and land[x][y] == '.':
                    visited[x][y] = False
                    s.append([x, y])

def dfs(src, visited, land, n, m):
    check_fence = False
    size = 1
    s = []
    s.append(src)

    if src[0] == 0 or src[0] == n - 1 or src[1] == 0 or src[1] == m - 1:
        check_fence = True
    while len(s) > 0:
        temp = s.pop()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if x in range(n) and y in range(m):
                if not visited[x][y] and land[x][y] == '.':
                    size += 1
                    visited[x][y] = True
                    s.append([x, y])
                    if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                        check_fence = True
    if check_fence:
        size = -1
    return size

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    visited = [None] * n
    land = [None] * n
    for i in range(n):
        land[i] = list(input())
        visited[i] = [False] * m

    lakes = []
    for i in range(n):
        for j in range(m):
            if land[i][j] == '.' and not visited[i][j]:
                visited[i][j] = True
                size = dfs([i, j], visited, land, n, m)
                if size != -1:
                    lakes.append(Lake(i, j, size))

    lakes.sort(key=lambda s: s.size)
    lake_fill = len(lakes) - k
    cell_fill = 0

    for i in range(lake_fill):
        cell_fill += lakes[i].size
        dfs_fill([lakes[i].x, lakes[i].y])
    print(cell_fill)

    # print land
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                print('*', end='')
            else:
                print('.', end='')
        print('')