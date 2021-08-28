"""
https://codeforces.com/problemset/problem/551/A

- ví dụ input 1: 1 3 3
    + hs 1 có điểm rating 1, hs 2 & 3 có điểm rating = nhau = 3
    + như v hs 2 và 3 đồng hạng 1, hs 1 đứng hạng 3
    => output là rank của hs theo mảng ban đầu: 3 1 1

- Input:
    + dòng 1: số học sinh
    + dòng 2: điểm rating của từng hs
- Output:
    + in ra xếp hạng của mỗi học sinh

IDEA:
- c1: thứ hạng = 1 + số người hơn mình. loop qua coi những ai cao hơn mình là đc.
- c2:
    + tạo 1 mảng rank để lưu rank của điểm.
    + vì ta chỉ quan tâm lần đầu gặp ptử đó thôi
    (vd 5 5 5 4 4 4, thì cả 3 cái 5 đều có rank = 1, có đc nhờ vào ptử đầu index = 0 => rank = index + 1,
    2 cái sau ko quan tâm. Tương tự vs 4, ta chỉ quan tâm 4 tại index = 3 -> rank = 4)
    => duyệt qua mảng a, gặp ptử nào đầu tiên (vị trí trong rank=0) thì cập nhật. mấy cái phía sau thì bỏ qua (vì ta chỉ quan tâm cái đầu)
"""

n = int(input())
a = list(map(int, input().split()))

## CÁCH 1: chưa tối ưu lắm
# for i in range(n):
#     cnt = 1
#     for j in range(n):
#         if a[i] < a[j]:
#             cnt += 1
#     print(cnt, end=' ')

## CÁCH 2:
rank = [0] * 2000
a_sorted = sorted(a, reverse=True)

for i in range(n):
    if rank[a_sorted[i]] == 0:
        rank[a_sorted[i]] = i + 1

for i in range(n):
    print(rank[a[i]], end=' ')
