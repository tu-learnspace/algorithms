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
- số lượng tháp là số thanh gỗ có chiều dài = nhau
- chiều cao là số lần lặp lại của thanh gỗ có chiều dài max
"""
n = int(input())
a = list(map(int,input().split()))

cnt = [0]*1001

for i in range(len(a)):
    cnt[a[i]] += 1

towers = max_tower = 0

for i in range(len(cnt)):
    if cnt[i] != 0:
        towers += 1
        max_tower = max(cnt[i], max_tower)

print(max_tower, towers)
