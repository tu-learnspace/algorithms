"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1552

- cho mảng a sắp xếp tăng dần
- lần lượt cho số b[i]. tìm phần tử nhỏ hơn nó và lớn nhất trong tập tìm đc & phần tử lớn hơn nó và nhỏ nhất trong tập tìm đc

IDEA:
- mảng đã đc sort tăng dần. ptử nhỏ hơn lớn nhất => nhở hơn cuối cùng. ptử lớn hơn nhỏ nhất => lớn hơn đầu tiên
"""

def bs_last_smaller(a, left, right, x):
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:      # thỏa nhỏ hơn rồi á
            res = mid
            left = mid + 1  # nhưng là cái cuối cùng chưa?
        else:
            right = mid - 1
    return res


def bs_first_larger(a, left, right, x):
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:          # thỏa lớn hơn rồi
            res = mid
            right = mid - 1     # nhưng chắc là cái đầu tiên chưa?
        else:
            left = mid + 1
    return res


n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = list(map(int, input().split()))
for i in range(q):
    low = a[bs_last_smaller(a, 0, n - 1, b[i])] if bs_last_smaller(a, 0, n - 1, b[i]) != -1 else 'X'
    upp = a[bs_first_larger(a, 0, n - 1, b[i])] if bs_first_larger(a, 0, n - 1, b[i]) != -1 else 'X'
    print(low, upp)


# code dưới này xài khoảng từ 0 đến n nên phức tạp vkl => bỏ đi
#
# def bs_last_smaller(a, left, right, x):
#     res = -1
#     while left < right:
#         mid = (left + right) // 2
#         if a[mid] < x:      # thỏa nhỏ hơn rồi á
#             res = mid
#             left = mid + 1  # nhưng là cái cuối cùng chưa?
#         else:
#             right = mid     # ở đây ta ko lấy right (cũng như ko lấy mid, vì nếu lấy mid thì mid ở if trên thỏa rồi)
#     return res
#
#
# def bs_first_larger(a, left, right, x):
#     res = -1    # theo lẽ thường nên là n, nhưng ở đây những TH x ko có trong mảng quy về -1 hết để in ra cho dễ
#     while left < right:
#         mid = (left + right) // 2
#         if a[mid] > x:      # thỏa lớn hơn rồi
#             res = mid
#             right = mid     # nhưng chắc là cái đầu tiên chưa? lẽ ra cập nhật right = mid - 1 (nhưng ta ko lấy right, cũng như ta ko lấy mid)
#         else:
#             left = mid + 1
#     return res
#
#
# n = int(input())
# a = list(map(int, input().split()))
# q = int(input())
# b = list(map(int, input().split()))
# for i in range(q):
#     low = a[bs_last_smaller(a, 0, n, b[i])] if bs_last_smaller(a, 0, n, b[i]) != -1 else 'X'
#     upp = a[bs_first_larger(a, 0, n, b[i])] if bs_first_larger(a, 0, n, b[i]) != -1 else 'X'
#     print(low, upp)
