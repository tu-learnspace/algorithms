"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3183

- cho vạch chiều cao các bậc thang
- cho năng lượng bản thân là k:
    + khi nhảy đúng k thì k bị giảm 1
    + nhảy dưới thì ko sao
    + ko nhảy độ cao lớn hơn k đc
- hãy tìm k thấp nhất để nhảy hết bậc thang

IDEA:
- mức năng lượng càng cao thì càng dễ leo đến bậc thang cuối. ngc lại, mức năng lượng càng thấp thì giảm khả năng leo đc tới bậc cuối
- mức năng lượng tối đa = bậc cao nhất (vì nhảy bậc thang = mức năng lượng thì mức năng lượng giảm đi 1. => TH tệ nhất (ko thể chia bậc thang nhỏ hơn) là các bậc thang có độ dài = nhau và = 1 và mức năng lượng = bậc cao nhất => đến bậc cao nhất là vừa hết năng lượng)
=> mức năng lượng nằm trong đoạn [1, max_height]
=> binary search trên đoạn này & kiểm tra
"""
def check(a, k):
    for i in range(n + 1):
        if a[i] - a[i-1] > k:       # bước nhảy quá lớn hơn năng lượng hiện có
            return False
        elif a[i] - a[i-1] == k:
            k -= 1
    return True


tc = int(input())
for i in range(tc):
    n = int(input())
    heights = [0] + list(map(int, input().split()))     # thêm [0] vì bắt đầu tại mặt đất xem như là bậc 0

    left = 1
    right = heights[n]                                  # max range là vị trí bậc cao nhất
    res = 0

    while left <= right:
        mid = (left + right) // 2
        if check(heights, mid):
            res = mid                                   # thỏa rồi nhưng có là min chưa? => thu hẹp right
            right = mid - 1
        else:
            left = mid + 1

    print('Case {}: {}'.format(i + 1, res))
