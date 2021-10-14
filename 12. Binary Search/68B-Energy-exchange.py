"""
https://codeforces.com/problemset/problem/68/B

- cho n bình điện. mỗi bình chứa ai đơn vị năng lượng
- muốn đạt mục tiêu năng lượng trong mỗi bình là như nhau
- có thể chuyển đổi năng lượng từ bình này sang bình khác. mỗi khi vận chuyển đi thì bị hao hụt k% lần
(vd: chuyển x từ bình A sang bình B thì bình A mất k năng lượng, còn bình B nhận x - x * k/100 năng lượng
- tìm mức năng lượng lớn nhất mà mỗi bình có thể có (lúc này mỗi bình có năng lượng bằng nhau)

IDEA:
- lượng năng lượng có thể là số thực
- gọi sumEnergy là tổng năng lượng ban đầu. m là năng lượng mỗi bình sau cùng. cần tim m lớn nhất?
=> tổng năng lượng trao đổi là n * m
- gọi xi là năng lượng bình đc chuyển đi, 1 bình chỉ có 2 TH xi:
    0       : năng lượng gốc dưới m (tức là ko chuyển đi mà nhận vào)
    ai - m   : năng lượng gốc lớn hơn m (chuyển đi 1 lượng để còn lại đúng m năng lượng)
=> sumTransfer = tổng các xi = tổng ai - m
=> sumLost = sumTransfer * k/100
- tổng năng lượng trao đổi = tổng năng lượng ban đầu - tổng năng lượng bị mất
    n * m = sumEnergy - sumLost

- giới hạn năng lượng của bình là từ 0 -> 1000. nhưng m có thể là số thực => đi dò m
- ta có: m = sumEnergy - sumLost / n
=> ta đi dò m, nếu:
    m < sumEnergy - sumLost / n   => tăng m (vẫn còn thừa năng lượng để phân bố)
    ngc lại: => giảm m (năng lượng ko đủ để phân bố)
=> xài binary search vs giới hạn [0, 1000]
- vì là số thực nên đề bài có cho sai số ko quá 10^-6 => điều kiện để chặt nhị phân
    sai số 10^-6 => mình phải đặt là 10^-7 để an toàn vì đôi khi nó tự làm tròn số
    vd: 0.00000014  => bị làm tròn xuống 0.0000001
        0.00000015  => bị làm tròn lên 0.0000002
"""
epsilon = 1e-7

n, k = map(int, input().split())
a = list(map(int, input().split()))

sumEnergy = sum(a)
left = min(a)                         # đặt = 0 cũng đc
right = max(a)                        # đặt = 1000 cũng đc

while right - left > epsilon:
    mid = (left + right) / 2

    sumTransfer = 0
    for ai in a:
        if ai > mid:                   # chỉ chuyển năng lượng từ những bình lớn hơn mức m (mid), còn dưới mức đó thì k cần
            sumTransfer += (ai - mid)

    sumLost = sumTransfer * k / 100

    if mid < (sumEnergy - sumLost) / n:
        left = mid + epsilon            # để left = mid và right = mid cũng được vì epsilon rất nhỏ (bth là để left = mid + 1, nhưng m ở đây là số thực, ko phải là các khoảng)
    else:
        right = mid - epsilon

print('{:.9f}'.format(left))             # in mid, left, right cũng đc vì thuật toán đảm bảo chênh lệch của cả 3 đủ sai số để chấp nhận đc
                                         # tuy nhiên với testcase: 1 0 thì mid bị undefined => tốt nhất in left
                                         #                         0