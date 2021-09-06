"""
https://codeforces.com/problemset/problem/540/C

- Trò chơi đi qua các ô băng và rớt xuống dưới để qua màn tiếp
- Đi vào ô bị nứt sẽ rớt xuống dưới tại vị trí đó
- Đi vào một ô cứng, ô đó sẽ thành ô nứt
- Cho điểm xuất phát và điểm kết thúc. hỏi có thể rớt xuống màn tiếp theo không

- Input:
    + dòng 1: n-số hàng, m-số cột của bàn cờ băng
    + n dòng tiếp theo hiển thị bàn cờ băng. '.' là ô cứng. 'X' là ô nứt
    + dòng tiếp theo: r1 c1-điểm xuất phát
    + dòng tiếp theo: r2 c2- vị trí ô phải rớt xuống
- Output: YES hoặc NO

IDEA:
- nếu end là ô nứt thì đi tới luôn, nếu end là ô cứng thì phải đi qua 2 lần (để thành ô nứt)
"""

def BFS(icecave, start, end):

    count = 0


n, m = map(int, input().split())

icecave = [None]*n
for i in range(n):
    icecave[i] = list(input())

start = end = [None]*2
start[0], start[1] = map(int, input().split())
end[0], end[1] = map(int, input().split())

BFS(icecave, start, end)