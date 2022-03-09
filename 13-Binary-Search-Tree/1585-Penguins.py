"""
https://acm.timus.ru/problem.aspx?space=1&num=1585

- danh sách các loại chim cánh cụt
- in ra loại nào có số lượng lớn nhất (input đảm bảo chỉ có 1 loại)

IDEA:
- xài BST lưu cặp <tên loại chim cánh cụt, số lượng>
- sort theo số lượng rồi in ra
"""

d = dict()

n = int(input())
for _ in range(n):
    line = input()
    if line not in d.keys():
        d[line] = 1
    else:
        d[line] += 1

max_peg = 0
name = ''
for key in d.keys():
    if d[key] > max_peg:
        max_peg = d[key]
        name = key

print(name)

