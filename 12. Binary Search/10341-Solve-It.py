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
=> f(x) là hàm nghịch biến trên tập xác định [0, 1]. Nghĩa là x0 > x1 thì f(x0) <= f(x1)

- kiểm tra vô nghiệm: x nằm ngoài [0, 1] thì kết luận vô nghiệm. Nghĩa là với bộ số p, q, r, s, t, u input => pt vô nghiệm nếu:
    f(0) < 0
    f(1) > 0
- range là [0, 1] => chặt nhị phân để tìm kiếm
- đề yêu cầu chính xác tới 4 chữ số thập phân (kết quả dạng: 0.0000x) => 10^-5 nhưng để phòng việc bị tràn số nên chọn chọn epsilon = 10^-6
"""
import math
epsilon = 1e-6


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
        