"""
https://codeforces.com/problemset/problem/334/B

- Vẽ 3 đường thằng x1,x2,x3 và y1,y2,y3 => đc 9 giao điểm, bỏ đi điểm chính giữa => 8 điểm respectable
- Cho sẵn 8 điểm. Hỏi có phải respectable ko?

- Input:
    + gồm 8 dòng dữ liệu là 8 điểm (x,y)
- Output: respectable hoặc ugly

IDEA:
- Kiểm tra coi có đúng 3 dọc vs 3 nganhg ko -> nếu ko chắc chắn là ugly
- Tạo 8 điểm từ 6 đường đó
- So sánh vs 8 điểm đề bài:
    + Trùng -> respectable
    + Ko trùng -> ugly
"""

# lưu các hoành độ, tung độ phân biệt => đây là các đường dọc và ngang (phải đủ 3 dọc 3 ngang phân biệt mới đc)
X = []
Y = []
points = []

for _ in range(8):
    x, y = map(int, input().split())
    points.append((x, y))
    if x not in X:
        X.append(x)
    if y not in Y:
        Y.append(y)

# kiểm tra đủ 3 hoành, 3 tung không
if len(X) != 3 and len(Y) != 3:
    print('ugly')
    exit()

# cần sort trước để so sánh ko bị thiếu
X.sort()
Y.sort()
points.sort()
index = 0

# sinh ra các điểm từ mảng X và Y
for x in range(3):
    for y in range(3):
        if x == 1 and y == 1:  # bỏ qua điểm chính giữa là vòng lặp thứ 2 của vòng lặp thứ 2
            continue
        if X[x] != points[index][0] or Y[y] != points[index][1]:
            print('ugly')
            exit()
        else:
            index += 1

print('respectable')