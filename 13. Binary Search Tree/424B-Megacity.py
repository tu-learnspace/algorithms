"""
https://codeforces.com/problemset/problem/424/B

- thành phố có dân số S người, trung tâm thành phố tại (0,0)
- có N điểm dân cư chứa một lượng k người
- chính quyền muốn mở rộng thành phố theo bán kính hình tròn, những điểm dân cư thuộc đường tròn sẽ đc gia tăng dân số
- thành phố là MegaCity nếu dân số ko ít hơn 1 triệu
- tìm bán kính mở rộng bé nhất để tp đạt chuẩn MegaCity, ko đc thì in ra -1

IDEA:
- nhận xét: một trong các điểm dân cư sẽ nằm trên đường tròn bán kính nhỏ nhất
- có tập location là khoảng cách từ (0,0) đến các điểm dân cư. Ta cần ánh xạ location sang mật độ dân cư tại điểm đó
- khoảng cách từ các điểm dân cư tới tâm (0,0) = sqrt( (x - 0)^2 + (y - 0)^2 ) = sqrt(x^2 - y^2)
=> thay vì lưu tọa độ (x,y) thì ta có thể lưu đại diện là x^2 - y^2 (ko nên lưu sqrt vì sẽ bị số thập phân)
- ta lưu <key, value> = <khoảng_cách^2, mật_độ_dân_số>
=> duyệt các cặp key,value. cộng dồn value vào s (dân số ban đầu), đến khi nào đủ 1 triệu thì lấy key ra => bán kính bé nhất
- lưu ý xài python thì phải sort key của dict
"""
import math
density = dict()                    # key,value = location,mật độ số dân

n, s = map(int, input().split())

for _ in range(n):
    x, y, k = map(int, input().split())
    dist = x * x + y * y
    if dist not in density.keys():
        density[dist] = k
    else:
        density[dist] += k

for dist in sorted(density.keys()):
    s += density[dist]
    if s >= 1000000:
        print(math.sqrt(dist))
        exit()

print('-1')




