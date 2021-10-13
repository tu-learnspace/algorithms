"""
https://www.spoj.com/problems/EKO/

- cần phải đốn M mét gỗ
- chọn ra chiều cao H cố định:
    các cây có độ cao a > H thì chặt đi sao cho bằng độ cao H. Phần dư nhận đc là H - a
    các cây có độ cao < H thì giữ nguyên
- tìm chiều cao H cao nhất sao cho nhận đc tổng phần dư ít nhất là M

IDEA:
- có thể thấy phải chọn 1 độ cao H nào đó để tổng gỗ lấy đc >= M
- nghĩa là cứ dò độ cao H sao cho vừa đủ lấy gỗ, nếu tăng H lên mà ko lấy đủ nữa thì kết luận H. Ngc lại, nếu chọn độ cao H nào đõ vẫn ko đủ lấy gỗ thì ta phải giảm H xuống
- các chiều H có tính liên tục, mỗi H ta có thể biết đc là có lấy đc đủ gỗ ko
=> tìm kiếm nhị phân (tìm kiếm bth cũng đc nhưng sẽ bị TLE)
"""
def check(h, m):
    wood = 0
    for x in a:
        if x > h:
            diff = x - h
            wood += diff
    if wood >= m:
        return True
    return False

n, m = map(int, input().split())
a = list(map(int, input().split()))

left = 1
right = max(a)
ans = 0

while left <= right:
    mid = left + (right - left) // 2
    if check(mid, m):       # thỏa số gỗ
        ans = mid
        left = mid + 1      # nhưng có chắc H cao nhất chưa
    else:
        right = mid - 1

print(ans)
