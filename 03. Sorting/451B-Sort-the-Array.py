"""
https://codeforces.com/problemset/problem/451/B

- liệu có đoạn l,r nào thuộc mảng a mà đảo nó lại thì mảng a đc sắp xếp tăng dần

- Input:
    + dòng 1: n là kích thước mảng a
    + dòng 2: mảng a
- Output:
    + yes hoặc no. nếu yes thì in ra 2 số nguyên l, r

IDEA:
- Sort mảng a rồi so sánh với mảng ban đầu => tìm đc vị trí khác biệt
- Tuy nhiên, chưa chắc mảng con đảo ngược sẽ tăng dần
=> thử đảo ngược mảng con vừa sắp xếp tăng dần, nếu nó trùng khớp với mảng con ban đầu => yes
- Đảo ngược mảng con: chỉ cần swap 2 ptử rìa, thu gọn vào chính giữa
"""

n = int(input())
a = list(map(int, input().split()))
l = r = 0
a_sorted = sorted(a)

# tìm vị trí đầu tiên left khác biệt
for i in range(n):
    if a[i] != a_sorted[i]:
        l = i
        break
# tìm vị trí đầu tiên right khác biệt
for i in range(n-1,-1,-1):
    if a[i] != a_sorted[i]:
        r = i
        break

# swap và so sánh
i, j = l, r
while i <= j:
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    i += 1
    j -= 1

if a_sorted == a:
    print('yes')
    print(l + 1, end=' ')
    print(r + 1, end='')
else:
    print('no')

