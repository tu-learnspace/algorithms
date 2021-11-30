"""
https://www.spoj.com/problems/PRO/

- có thùng phiếu chứa các hóa đơn. siêu thị có đợt khuyến mãi
- mỗi cuối ngày đợt khuyến mãi, siêu thị chọn hóa đơn có tổng tiền lớn nhất & nhỏ nhất
- khách hàng nhận đc tiền thưởng = chênh lệnh hóa đơn lớn nhất và nhỏ nhất
- hóa đơn nào đã đc chọn thì k đc bỏ lại vào thùng phiếu, các phiếu còn lại vẫn tiếp tục đc tgia chương trình
- đề bài đảm bảo luôn luôn có ít nhất 2 hóa đơn trong thùng
- tính chi phi mà siêu thị phải bỏ ra để thưởng tiền khách hàng

- input:
    + dòng 1: n-số ngày của đợt khuyến mãi
    + n dòng tiếp theo: a a1 a2 a3 ... (với a là số hóa đơn trong ngày, ai là số tiền của các hóa đơn)
- ouput: chi phí cho đợt khuyến mãi

IDEA:
- mỗi ngày cần pop ra min và max trong thùng => xài minheap & maxheap
- với mỗi hóa đơn thì push vào trong cả min heap & max heap
- điều quan trọng là đồng bộ 2 heap khi pop ra (pop ra từ heap này rồi nhưng heap kia còn ở trỏng)
=> mỗi hóa đơn tạo 1 id rồi dùng dict để đánh dấu hóa đơn có id đó đã đc lấy ra
"""
import heapq
maxh = []
minh = []
deleted = dict()

money = id = 0
n = int(input())
for _ in range(n):
    a = list(map(int, input().split()))

    for x in a[1:]:
        id += 1
        heapq.heappush(maxh, (-x, id))
        heapq.heappush(minh, (x, id))
        deleted[id] = False

    # đồng bộ (đã deleted thì pop ra)
    while deleted[maxh[0][1]]:
        heapq.heappop(maxh)
    while deleted[minh[0][1]]:
        heapq.heappop(minh)

    # pop ra để tính toán
    deleted[maxh[0][1]] = deleted[minh[0][1]] = True
    money += -heapq.heappop(maxh)[0] - heapq.heappop(minh)[0]

print(money)
