"""
https://www.spoj.com/problems/UCV2013H/

- Vết dầu loang đc hiển thị bằng ảnh nhị phân. Có vết dầu thì là 1, ko có là 0
- Hai pixel liền kề có cùng vết loang nếu như nằm cùng một hàng hoặc cùng một cột
- Kích thước vết loang là tổng số ô 1.

- Input:
    + chứa các testcase. Mỗi testcase có:
        + dòng 1: N-số hàng, M-số cột của bức ảnh. Nếu M = N = 0 thì hết testcase
        + N hàng tiếp theo chứa M cột thông tin của bức ảnh
- Output:
    + dòng 1: số lượng vết loang
    + các dòng còn lại (theo thứ tự tăng dần kích thước):
        [kích thước vết loang]: [số lượng vết loang có kích thước này]
    vd:
    2   (có 2 vết loang)
    1 2 (số vết loang có kích thước 1 là 2 vết)

IDEA:
- duyệt bfs từ trên xuống dưới image:
    + nếu gặp số 1 thì đưa vào bfs để loang ra hết các chỗ có thể đi:
        - mỗi lần loang thì +1 vô size, loang xong hết thì return size của bãi loang
    + nếu gặp số 0 hoặc số 1 đã visited thì skip
"""
from queue import Queue
# đối vs các bài dạng di chuyển quanh ma trận có thể dùng như thế này
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(image, visited, start, N, M):
    size = 0
    q = Queue()
    q.put(start)
    visited[start[0]][start[1]] = True

    while not q.empty():
        temp = q.get()

        size += 1
        for i in range(4):
            r = temp[0] + dx[i]
            c = temp[1] + dy[i]
            if r in range(N) and c in range(M):
                if image[r][c] == 1 and visited[r][c] == False:
                    q.put([r, c])
                    visited[r][c] = True

    return size

if __name__ == '__main__':
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        count = 0
        res = [0] * (250 * 250 + 5)
        visited = [None] * N
        image = [None] * N

        for i in range(N):
            image[i] = list(map(int, input().split()))
            visited[i] = [False] * M

        for i in range(N):
            for j in range(M):
                if visited[i][j] or image[i][j] == 0:
                    continue
                else:
                    start = [i, j]
                    res[BFS(image, visited, start, N, M)] += 1
                    count += 1

        print(count)
        for i in range(len(res)):
            if res[i]:
                print(i, res[i])
