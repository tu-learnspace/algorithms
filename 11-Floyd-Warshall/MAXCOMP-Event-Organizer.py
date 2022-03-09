"""
https://www.codechef.com/problems/MAXCOMP

- có n yêu cầu Po tổ chức sự kiện. tất cả yêu cầu tổ chức trong 2 ngày cuối tuần
- giờ của ngày thứ 7 đc đánh số từ 0 - 24, chủ nhật đc đánh số từ 24 - 48 (vd 10h sáng ngày chủ nhật đc đánh số là 34)
- mỗi yêu cầu gồm:
    + s: thời gian bắt đầu
    + e: thời gian kết thúc
    + c: thù lao nhận đc
- khi tổ chức sự kiện thì Po phải có mặt suốt (tức là khoảng thời gian tổ chức sự kiện ko đc đè lên nhau), sự kiện mới có thể bắt đầu ngay khi sự kiện kia kết thúc
- Po sẽ nhận yêu cầu sao cho thù lao nhận đc tối đa. Tìm số tối đa của thù lao này

IDEA:
- 48 giờ => ma trận 48x48 đại diện thù lao của các sự kiện theo mốc giờ [start][end], khởi tạo = 0
- tìm đường đi lớn nhất giữa các cặp đỉnh (các sự kiện) => dùng floyd
- vì các sự kiện không được đè lên nhau => điểm trung gian K phải nằm trong khoảng điểm I-J thì mới cập nhật
- muốn tìm thù lao lớn nhất từ 0h đến 48h => dist[0][48]
"""
MAX = 48

def floyd(n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i <= k <= j:                         # nếu có thể tách 1 sự kiện lớn thành 2 sự kiện nhỏ đề có thù lao cao hơn thì phải thỏa ko bị đè nhau
                    if dist[i][j] < dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]



tc = int(input())
for _ in range(tc):
    dist = [[0] * (MAX + 1) for _ in range(MAX + 1)]    # thời gian tổ chức các sự kiện từ thời gian i -> j

    n = int(input())
    for _ in range(n):
        s, e, c = map(int, input().split())
        if c > dist[s][e]:                              # check ở đây vì có thể có các sự kiện trùng nhau nhưng ta chỉ lấy sự kiện có thù lao cao nhất
            dist[s][e] = c

    floyd(MAX + 1)
    print(dist[0][MAX])