"""
https://codeforces.com/problemset/problem/691/A

 - Tất cả các nút của áo phải được cài, để hở 1 nút duy nhất tạo style. Nếu chỉ có 1 nút thì phải cài (ko cài sao mặc).
 - Tuân theo quy luật trên thì print YES, else NO

IDEA:
 - TH 1 nút thì xét có cài hay ko.
 - TH còn lại thì đếm xem nếu số nút đc cài = tổng nút - 1 (để hở 1 nút) thì ok.
"""

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        if a[0] == 1:
            print('YES')
        else:
            print('NO')
    else:
        count = 0
        for i in range(n):
            if a[i] == 1:
                count += 1
        if count == n - 1:
            print('YES')
        else:
            print('NO')
