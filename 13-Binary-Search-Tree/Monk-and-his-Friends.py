"""
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/monk-and-his-friends/

- có N học sinh trong phòng, người thứ i có Ai viên kẹo
- sẽ có M học sinh nữa tới. học sinh mới vào thì muốn ngồi cùng với bạn có số kẹo = mình
- tại mỗi thời điểm có học sinh mới vào, trả lời 'YES' hoặc 'NO' nếu có thể có bạn ngồi cùng

IDEA:
- xài BST, nếu phần tử đã có trong BST rồi thì in 'YES', ko thì in 'NO'
"""

tc = int(input())

for _ in range(tc):
    s = set()
    n, m = map(int, input().split())
    line = list(input().split())

    for i in range(n):
        s.add(line[i])

    for i in range(n, n + m):
        if line[i] in s:
            print('YES')
        else:
            print('NO')
            s.add(line[i])

