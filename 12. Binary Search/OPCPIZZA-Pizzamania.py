"""
https://www.spoj.com/problems/OPCPIZZA/

- có n bạn, mỗi ng có 1 số tiền (có thể âm), và pizza giá m
- hỏi có tối đa bao nhiêu cặp bạn có thể mua pizza bằng đúng giá pizza

IDEA:
- với số tiền mỗi người => tìm đc số tiền ng còn lại
=> dùng binary search để tìm người còn lại (ko đc trùng người kia)
- tuy nhiên 1 cặp sẽ bị lặp lại 2 lần => thu nhỏ khoảng tìm theo mỗi lần tìm
"""
def bs(a, left, right, friend1_id, friend2_money):
    while left <= right:
        mid = (left + right) // 2
        if friend2_money == a[mid] and friend1_id != mid:
            return 1
        elif friend2_money < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0


tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n):
        friend = m - a[i]
        res += bs(a, i, n -1, i, friend)
    print(res)






