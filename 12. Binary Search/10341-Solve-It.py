"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1282

- giải phương tình, tìm x:
    p.e^(-x) + q.sin(x) + r.cos(x) + s.tan(x) + t.x^2 + u = 0
- với   0 <= x <= 1
        0 <= p, r <= 20
        -20 <= q, s, t <= 0
- in ra làm tròn tới 4 chữ số thập phân

IDEA:
- đề bài cho dữ kiện các biến => có thể hàm f(x) có 1 đặc trưng nào đó
- ta đạo hàm f'(x) kết hợp với dữ kiện => f'(x) <= 0. f'(x) = 0 khi và chỉ khi x,p,r,q,s,t = 0, nghĩa là u = 0 => ko thể tìm x
=> f'(x) < 0
=> f(x) là hàm nghịch biến trên tập xác định [0, 1]. Nghĩa là x0 > x1 thì f(x0) < f(x1)

- pt có nghiệm tại f(x) = 0. Như vậy, pt vô nghiệm nếu: f(x) < 0 hoặc f(x) > 0. lại có f(x) nghịch biến
- mà x chạy trong khoảng [0,1], nên ta có thể xét:
    nếu f(1) > 0 thì ko thể có x là nghiệm đc. vd f(0.99) càng > hơn 0 nữa
    nếu f(0) < 0 thì ko thể có x là nghiệm đc. vd f(0.01) càng < hơn 0 nữa
    => PT vô nghiệm trong 2 TH f(1) > 0 và f(0) < 0

- range là [0, 1], nghiệm có thể là số thực
=> chặt nhị phân trên range để tìm kiếm
"""
import math
epsilon = 1e-9


def calculate(p, q, r, s, t, u, x):
    return p*math.exp(-x) + q*math.sin(x) + r*math.cos(x) + s*math.tan(x) + t*x*x + u


while True:
    try:
        p, q, r, s, t, u = map(int, input().split())

        if calculate(p, q, r, s, t, u, 1.0) > 0 or calculate(p, q, r, s, t, u, 0.0) < 0:
            print('No solution')
            continue

        x = -1
        left = 0.0000                                   # đề yêu cầu 4 chữ số thập phân
        right = 1.0000

        while right - left > epsilon:
            mid = (right + left) / 2.0
            res = calculate(p, q, r, s, t, u, mid)
            if res > 0 + epsilon:                       # f(x) > 0 nghĩa là ta cần tăng x để f(x) giảm về 0
                left = mid + epsilon
            else:
                right = mid - epsilon

        print('{:0.4f}'.format(left))

    except EOFError:
        break
