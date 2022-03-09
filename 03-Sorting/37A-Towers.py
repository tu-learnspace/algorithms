"""
https://codeforces.com/problemset/problem/37/A

- 2 thanh gỗ cùng độ dài có thể xếp chồng lên nhau
- muốn xây tháp từ các thanh này
- phải sử dụng hết toàn bộ thanh gỗ.

- Input:
    + dòng 1: số lượng thanh gỗ
    + dòng 2: chiều dài các thanh gỗ
- Output:
    + 2 số lần lượt là chiều cao max của tháp & tổng số lượng tháp.

IDEA:
c1:
- số lượng tháp là số thanh gỗ có chiều dài = nhau
- chiều cao là số lần lặp lại của thanh gỗ có chiều dài max

c2: tối ưu hơn
- sort các thanh gỗ tăng dần rồi duyệt
- mỗi lần có 2 thanh kế nhau khác nhau => tăng số tháp lên 1
- đồng thời cũng ghi nhận lại số thanh gỗ bằng nhau để so sánh tìm ra tháp max
"""
# c1:
# n = int(input())
# a = list(map(int,input().split()))
# cnt = [0]*1001
# for i in range(len(a)):
#     cnt[a[i]] += 1
#
# towers = max_tower = 0
# for i in range(len(cnt)):
#     if cnt[i] != 0:
#         towers += 1
#         max_tower = max(cnt[i], max_tower)
#
# print(max_tower, towers)

# c2:
n = int(input())
bars = list(map(int, input().split()))
bars.sort()

n_towers = max_height = cur_height = 1

for i in range(1, n):
    if bars[i] == bars[i - 1]:
        cur_height += 1
        max_height = max(max_height, cur_height)
    else:       # qua loại tháp mới => tăng số lượng tháp lên 1, reset cur_height
        n_towers += 1
        cur_height = 1

print(max_height, n_towers)