"""
https://www.spoj.com/problems/ALLIZWEL/

- Kiểm tra xem có thể tạo chuỗi 'ALL IZZ WELL' từ ma trận cho trước không
- Tạo: nghĩa là đi từ ô bất kỳ tới các ô lân cận (đi chéo được) để tạo ra chuỗi

- input:
    + dòng 1: t-số testcase. mỗi testcase có:
        - dòng 1: R C-số hàng, cột của ma trận
        - R dòng tiếp theo: biểu diễn ma trận
        - dòng trống
- output: với mỗi testcase, in 'YES' nếu tạo đc, ngc lại 'NO'

IDEA:
- duyệt brute-force toàn mảng khi bắt gặp chữ 'A' thì duyệt dfs tìm chuỗi (vì đây là tìm kiếm lần lượt theo chuỗi, đường đi, nên phải dfs - duyệt theo chiều sâu)
- khi đi tới con đường cụt thì nhớ bỏ con đường đó (reset lại visited trên con đường đó là False hết) => nên xài recursion
- nên xài recursion vì implement dễ hơn (ở khúc khi tới ô đó mà ko còn đường đi nữa thì quay lại check visited là False, nếu xài stack cài sẽ hơi rối)

- Useful testcase:
1
7 8
AWIA.AZA
IWZWZIWI
IIEZLLEA
AALIWAAZ
EEZEIEZI
EILWLEE.
Z.EAEAZI
"""
import sys
sys.setrecursionlimit(10 ** 6)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
end = 'ALLIZZWELL'  # chuỗi đích

def dfs(src, visited, maze, R, C, count):
    global check

    # chốt chặn ở đầu, để khi con đường nào cụt (count != 9) thì ko implement đống code phía dưới
    if count == 9:      # biến đếm trong chuỗi đích, = 9 là đi tới chữ cuối cùng rồi
        check = True
        return

    for i in range(8):
        r = src[0] + dx[i]
        c = src[1] + dy[i]
        if r in range(R) and c in range(C) and maze[r][c] == end[count + 1] and not visited[r][c]:  # ô tiếp theo thỏa là chữ cái cần tìm tiếp theo
            visited[r][c] = True    # đang viếng thăm ô đó
            dfs([r, c], visited, maze, R, C, count + 1)
            visited[r][c] = False   # tới đc dòng này là viếng nó rồi mà quay ra (vẫn chưa thỏa count = 9), nghĩa là đường cụt rồi, phải bỏ con đường đó (đánh dấu False các ô)


if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        R, C = map(int, input().split())
        maze = [None] * R
        visited = [None] * R
        for i in range(R):
            maze[i] = list(input())
            visited[i] = [False] * C

        check = False
        for i in range(R):
            for j in range(C):
                if maze[i][j] == 'A':
                    dfs([i, j], visited, maze, R, C, 0)
                    if check:
                        break
            if check:
                break

        if check:
            print('YES')
        else:
            print('NO')

        blank = input()