"""
https://lightoj.com/problem/guilty-prince

- Chỉ có thể đi trên đất liền
- '.' - đất
- '#' - nước
- '@' - vị trí ban đầu của hoàng tử (xuất hiện duy nhất một lần trong bộ dữ liệu)
- Cho 1 map, tính toán số ô đất liền có thể đi được

- Input:
    + dòng 1: số testcase
    + với mỗi test case:
        + dòng 1: W,H: độ dài x,y của map
        + H dòng tiếp theo chứ W ký tự là map
- Output: in ra số lượng đi được của mỗi testcase

IDEA:
- y chang bài validate the maze :)
"""
from queue import Queue


def BFS(maze, start, W, H):
    visited = [None] * W
    for i in range(W):
        visited[i] = [False] * H
    q = Queue()
    q.put(start)
    count = 0

    while not q.empty():
        temp = q.get()

        if temp[0] < 0 or temp[0] >= W or temp[1] < 0 or temp[1] >= H:
            continue
        else:
            if visited[temp[0]][temp[1]]:
                continue

        visited[temp[0]][temp[1]] = True

        if maze[temp[0]][temp[1]] == '.' or maze[temp[0]][temp[1]] == '@':  # able to move
            count += 1
            q.put([temp[0] + 1, temp[1]])
            q.put([temp[0] - 1, temp[1]])
            q.put([temp[0], temp[1] + 1])
            q.put([temp[0], temp[1] - 1])

    return count


if __name__ == '__main__':
    testcase = int(input())
    for tc in range(testcase):
        # read input
        H, W = map(int, input().split())
        maze = [None] * W
        for i in range(W):
            maze[i] = list(input())

        # find start
        start = []
        for i in range(W):
            for j in range(H):
                if maze[i][j] == '@':
                    start = [i, j]

        print('Case', tc + 1, end='')
        print(':', end=' ')
        print(BFS(maze, start, W, H))


