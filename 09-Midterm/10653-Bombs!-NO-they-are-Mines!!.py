from queue import Queue
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start, end):
    q = Queue()
    q.put(start)
    visited[start[0]][start[1]] = True
    dist[start[0]][start[1]] = 1

    while not q.empty():
        temp = q.get()

        for i in range(4):
            nextx = temp[0] + dx[i]
            nexty = temp[1] + dy[i]
            if nextx in range(R) and nexty in range(C):
                if maze[nextx][nexty] == False and visited[nextx][nexty] == False:
                    visited[nextx][nexty] = True

                    if nextx == end[0] and nexty == end[1]:
                        return dist[temp[0]][temp[1]]

                    dist[nextx][nexty] = dist[temp[0]][temp[1]] + 1
                    q.put([nextx, nexty])


while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    maze = [None] * R
    for i in range(R):
        maze[i] = [False]*C

    rows = int(input())
    for _ in range(rows):
        a = list(map(int, input().split()))
        row = a[0]
        bombs = a[1]
        for i in range(bombs):
            maze[row][a[i+2]] = True

    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    visited = [None] * R
    dist = [None] * R
    for i in range(R):
        visited[i] = [False] * C
        dist[i] = [-1] * C

    print(bfs(start, end))



