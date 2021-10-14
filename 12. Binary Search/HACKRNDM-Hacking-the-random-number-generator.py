"""
https://www.spoj.com/problems/HACKRNDM/

- nhận vào n số và k (n, k >=1). hãy cho biết số lượng cặp số có chênh lệch giá trị là k
- tất cả giá trị nằm trong kiểu dữ liệu số nguyên

IDEA:
- tìm 2 số a, b sao cho a - b = k => b = a - k
=> nghĩa là với mỗi số a, ta xem a - k có tồn tại trong mảng ko
=> dùng binary search
- lưu ý ta chỉ cần tìm a - k hoặc a + k thôi, vì tìm cả 2 sẽ bị đếm trùng
(vd: số (a) ta chỉ tìm (a) + k thì tới số (a+k) ta chỉ cần tìm (a+k) + k thôi, tìm (a+k) - k sẽ bị trùng lại số a)
"""

def bsearch(x):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False


n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

pairs = 0
for x in a:
    if bsearch(x + k):
        pairs += 1

print(pairs)

