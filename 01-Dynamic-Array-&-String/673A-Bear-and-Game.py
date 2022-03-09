"""
https://codeforces.com/problemset/problem/673/A

- Một trận đấu dài 90 phút.
- Nếu 15 phút liên tiếp boring thì tắt TV.
- Biết đc N mốc thời gian interesting -> tính số thời gian xem TV.
- Input:
    + dòng 1: số lượng mốc interesting
    + dòng 2: danh sách mốc interesting
- Output: số phút coi.

IDEA:
- cho 1 biến timestamp là mốc interesting (coi đến mốc đó), init = 0
- 2 khoảng interesting lớn > 15 -> boring enough to turn off tv
THĐB:
    + nếu chỉ có 1 mốc thời gian & <= 15 -> vẫn phải coi thêm ít nhất 15 phút nữa (xem coi nó có đủ chán ko)
    + mốc ban đầu quá lớn (>15) -> chỉ coi 15 phút đầu thôi, ai rảnh coi nữa.
    + nếu mốc cuối cùng quá gần 90 -> coi tối đa 90 thôi (vd: mốc 85 -> 85+15>90 nhưng chỉ coi tối đa 90)
"""

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))

    timestamp = 0

    if n == 1 and t[0] <= 15:
        timestamp = t[0] + 15
    elif t[0] >= 16:
        timestamp = 15
    else:
        for i in range(n):
            if t[i] - timestamp > 15:  # boring enough to off
                timestamp += 15
                break
            else:
                timestamp = t[i]

        if timestamp == t[n - 1]:  # TH mốc cuối thì phải + thêm 15 (vì trong vòng for chưa cộng)
            timestamp += 15  # nếu lỡ cộng lố 90 thì có if ở dưới chặn

        if timestamp > 90:
            timestamp = 90

    print(timestamp)
