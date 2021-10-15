"""
https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/

- Cho dãy số A có N số nguyên.
- Phân loại dãy đó thành:
    Good: bao gồm đúng X giá trị khác nhau
    Bad: ít hơn X giá trị khác nhau
    hoặc Average: nhiều hơn X giá trị khác nhau

IDEA:
- Ta có Ai rất lớn (<= 10^9) => ko thể dùng mảng lưu bth đc
=> dùng BST lưu trữ
=> dễ dàng biết đc có giá trị khác nhau (BST chỉ lưu giá trị khác nhau)
- ta chỉ cần so sánh kích thước của cây BST với X
"""

tc = int(input())

for _ in range(tc):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    s = set()
    for i in a:
        s.add(i)

    if len(s) == x:
        print('Good')
    elif len(s) < x:
        print('Bad')
    else:
        print('Average')


