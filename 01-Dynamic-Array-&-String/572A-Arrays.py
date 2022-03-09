"""
https://codeforces.com/problemset/problem/572/A

- Cho 2 mảng integer, sort tăng dần.
- Chọn K ptử trong A, M ptử trong B
- Does any of K < any of M ?
Input:
    + dòng 1: arr size A, B
    + dòng 2: K, M
    + dòng 3: arr A
    + dòng 4: arr B
Output:
    + làm đc thì print YES, else NO
VD:
    + 1 2 3
    + 3 4 5
    + k = 2, m = 1
    -> có thể chọn 1, 2 luôn < 3

    + 1 2 3
    + 3 4 5
    + k = 3, m = 3
    -> ko đc vì 3 < 3 sai
IDEA:
 - đề đúng thì ta luôn chọn arr ptử nhỏ nhất của A so với arr ptử lớn nhất của B
 -> chỉ cần so sánh max arr đã chọn của A (ptử cuối) và min arr đã chọn của B là đc
    + vd: k=3,m =3, A [1 2 3] và B [3 4 5 6] thì chỉ cần so sánh 3 < 4
"""
# má tức quá t lặp 2 vòng for chi rồi để time limit exceeded

if __name__ == '__main__':
    na,nb = map(int, input().split())
    k,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a[k - 1] < b[nb - m]:
        print('YES')
    else:
        print('NO')
