"""
https://codeforces.com/problemset/problem/224/B

- Có dãy số nguyên A1, A2, ... An
- Hãy tìm đoạn con tối thiểu [L,R] có chứa đúng K số nguyên phân biệt
- Đoạn con tối thiểu nghĩa là ko tồn tại đoạn bé hơn nằm trong nó cũng thỏa điều kiện => tức là ko thể thu gọn đc nữa
- Nếu có nhiều đoạn thì đoạn [L,R] ko nhất thiết là đoạn ngắn nhất
- Chỉ số bắt đầu từ 1

- Input:
    + Dòng 1: N và K
    + Dòng 2: chứa N số nguyên biểu diễn dãy số
- Output:
    + 1 dòng gồm 2 số nguyên L, R. Nếu ko tìm đc in -1 -1

IDEA:
- Có thể thấy mảng ko thể thu gọn tức là 2 ptử ngoài rìa phải là duy nhất trong mảng
- Đầu tiên dùng 1 con trỏ để tìm mảng chứa đủ phần tử phân biệt
- Sau đó dùng 1 con trỏ để thu gọn mảng. Vì dừng ngay khi đủ số ptử phân biệt => ko cần thu gọn biên phải
VD: 1 2 2 1 2 3 4 5 => [ 1 2 2 1 2 3 ] => [ 2 2 1 2 3 ] => [ 2 1 2 3 ] => [ 1 2 3 ]

- Useful test-case:
    3 1
    1 1 1
->  1 1
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))

# mảng để đếm xem số i có xuất hiện chưa (nếu = 0 nghĩa là gặp ptử mới)
count = [0] * (10 ** 5 + 5)
unique = 0
start = end = 0

for i in range(n):
    if count[a[i]] == 0:
        unique += 1
    count[a[i]] += 1

    # thu gọn bên trái
    if unique == k:
        for j in range(i + 1):
            if count[a[j]] == 1:        # giá trị là duy nhất trong mảng đang xét
                print(j + 1, i + 1)
                exit()
            count[a[j]] -= 1

print(-1, -1)




