"""
https://codeforces.com/problemset/problem/892/B

- Có n người có tội
- Người thứ i có chiếc móc vuốt độ dài Li
- Khi chuông điểm, tất cả sẽ giết người đứng trước họ
- Người i giết đc người j:
    + i > j (đứng sau)
    + j >= i - Li (vị trí j nào lớn hơn sẽ chết => vị trí j tối thiểu)
    => người đứng sau giết các người kề trc, và giết số người = độ dài vuốt
- In ra số người còn sống

- Input:
    + Dòng 1: số người có tội
    + Dòng 2: n số nguyên L là độ dài vuốt của người tại vị trí đó
- Output: số người còn sống sau khi chuông điểm

IDEA:
- Có thể tính số người bị giết, lấy tổng trừ đi ra số người còn sống
- Sử dụng thêm biến last để biết đc chỗ đó là người chết hay sống (chỉ khi j và last chênh lệch mới có người chết)
"""
n = int(input())
l = list(map(int, input().split()))
die = 0
last = n - 1    # vị trí cuối cùng của người chết

for i in range(n-1, -1, -1):
    last = min(last, i)             # last giảm bth thì j cũng giảm theo (j = i)
    die_pos = max(0, i - l[i])      # ngăn last bị âm

    if last > die_pos:              # last giảm nhanh quá (ko theo i) => tức là vị trí đó có người có vuốt > 0
        die += last - die_pos       # cập nhật người chết
        last = die_pos              # j nhảy đến vị trí giết cuối

print(n-die)


