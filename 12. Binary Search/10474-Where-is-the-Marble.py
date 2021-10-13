"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1415

- có n viên bi. mỗi viên bi có con số
- sắp xếp bi theo thứ tự tăng dần
- với mỗi truy vấn x, xác định vị trí số x đầu tiên trong dãy bi. nếu k có in ra x not found

IDEA:
- binary search first bth, tìm phần tử >= đầu tiên
- lưu ý vì nếu phần tử ko có trong mảng thì phải trả ra ko có (chứ ko phải trả ra vị trí đầu tiên > đã cài đặt mẫu)
=> phải xét cả 3 TH của a[mid]: == x, > x, < x
"""


def binarysearch(a, x):
    left = 0
    right = n - 1
    pos = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            pos = mid
            right = mid - 1
        elif a[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return pos


tc = 1
while True:
    n, q = map(int, input().split())
    if n == q == 0:
        break
    a = []
    for _ in range(n):
        a.append(int(input()))

    a.sort()

    print("CASE# {}:".format(tc))
    for _ in range(q):
        x = int(input())
        pos = binarysearch(a, x)
        if pos != -1:
            print('{} found at {}'.format(x, pos + 1))
        else:
            print('{} not found'.format(x))

    tc += 1
