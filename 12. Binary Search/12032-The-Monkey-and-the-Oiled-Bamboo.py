"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3183

- cho vạch chiều cao các bậc thang
- cho năng lượng bản thân là k:
    + khi nhảy đúng k thì k bị giảm 1
    + nhảy dưới thì ko sao
    + ko nhảy độ cao lớn hơn k đc
- hãy tìm k min để nhảy hết bậc thang

IDEA:
- tìm k => cần ước lượng range của k
=> xét đc range của k là từ 0 -> vạch chiều cao của bậc cao nhất (giả dụ TH tệ nhất là tất cả các vạch đều có độ dài = nhau, tốn nhiều năng lượng nhất)
- các vạch bậc thang nghiễm nhiên sắp xếp tăng dần
=> binary search trên đoạn này & kiểm tra:
    - những bậc thang nhỏ hơn thì ko sao vì ko ảnh hưởng năng lượng.
    - những bậc thang cùng độ cao vs bậc xa nhất?
    - những bậc thang lớn hơn k?
=> loop qua tất cả bậc thang, xem với k hiện tại có đi hết đc bậc thang hay ko (nếu có bậc thang lớn hơn thì ko đi đc, còn nếu có bậc thang = thì - k đi 1
=> nếu k chưa đủ tốt, thu hẹp left lại để tăng k lên
"""
def check_fail(a, k):
    for i in range(n - 1):
        if a[i + 1] - a[i] > k:     # k ko đủ để đi tiếp bậc thang
            return True
        elif a[i + 1] - a[i] == k:
            k -= 1

tc = int(input())
for i in range(tc):
    n = int(input())
    heights = [0] + list(map(int, input().split()))     # thêm [0] vì mặt đất xem như là bậc 0

    k = 0
    left = 1
    right = heights[n - 1]
    while left <= right:
        mid = (left + right) // 2

        if check_fail(heights, mid):
            left = mid + 1
        else:
            k = mid                     # thỏa rồi đó
            right = mid - 1             # nhưng chắc là nhỏ nhất chưa?

    print('Case {}: {}'.format(i + 1, k))
