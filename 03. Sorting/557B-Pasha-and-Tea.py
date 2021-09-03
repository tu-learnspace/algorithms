"""
https://codeforces.com/problemset/problem/557/B

- Bình trà dung tích tối đa W. Có 2N tách trà, mỗi tách trà có dung tích khác nhau
- Có N nam và N nữ tham gia buổi tiệc. Nam đc rót lượng trà gấp đôi nữ
- Vì Pasha là người hào phóng, hãy tính lượng trà tối đa cần chuẩn bị (vẫn phải thỏa các điều kiện)

- Input:
    + dòng 1: số N-số lượng nam/nữ và W-dung tích ấm trà
    + dòng 2: dãy ai-dung tích mỗi tách trà
- Output: lượng trà lớn nhất cần chuẩn bị

IDEA:
- Lượng trà nam gấp đôi nữ => để tối ưu thì phân nửa ly có dung tích lớn cho nam, phần còn lại cho nữ
- Dung tích ly của mọi người trong phái = dung tích ly người nhỏ nhất trong phái
- Đặt m là lượng trà của người nữ => 2m là lượng của người nam. Ta có:
    + 2m <= x
    + m <= y
    => m tối đa sẽ là min(x/2,y)
"""
n, w = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

m = min(a[0], a[n]/2)
tea = 3*m*n
max_tea = min(tea, w)  # ko được vượt quá dung tích ấm trà
print(max_tea)
