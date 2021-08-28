"""
https://codeforces.com/problemset/problem/451/B

- liệu có đoạn l,r nào thuộc mảng a mà đảo nó lại thì mảng a đc sắp xếp tăng dần
- mảng có đoạn [l,r] là liên tiếp [l, l+1, ..., r]
- đảo lại: mảng thành [1,2, ..., l-2, l-1, r, r-1, ..., l+1, l, r+1, r+2, ..., n-1, n]

- Input:
    + dòng 1: n là kích thước mảng a
    + dòng 2: mảng a
- Output:
    + yes hoặc no. nếu yes thì in ra 2 số nguyên l, r

IDEA:
tìm đoạn giảm, nếu ptử đầu tiền của đoạn giảm > ptử kề sau ptử cuối đoạn giảm hoặc ngc lại -> false
"""

n = int(input())
a = list(map(int,input().split()))

check = False
end = start = 0

for i in range(len(a)-1):
    start = i
    while a[i] < a[i+1]:
        end += 1
        i += 1

