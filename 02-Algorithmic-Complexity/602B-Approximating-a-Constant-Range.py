"""
https://codeforces.com/problemset/problem/602/B

- Dãy N gồm A1,...,An. Đảm bảo |Ai+1 - Ai| <= 1 (khoảng cách giữa 2 điểm nhỏ hơn bằng 1)
- Tìm khoảng sao cho tất cả giá trị trong khoảng đều ko có chênh lệch hơn 1

- Input:
    + dòng 1: chứa N là độ dài dãy
    + dòng 2: n số nguyên A1,...,An
- Output: in ra độ dài lớn nhất của một khoảng gần như ko đổi của dãy

IDEA:
- Phát biểu lại bài toán: tìm đoạn chỉ chứa 2 phần tử phân biệt lớn nhất
- Mở rộng đoạn bằng cách sử dụng biến i cho tới khi nào đoạn của ta có số lượng phần tử phân biệt lớn hơn 2,
- Lúc này ta tiến hành rút ngắn đoạn bằng cách đưa j chạy ngược lên. Thực hiện tương tự cho đến hết mảng.
"""

n = int(input())
a = list(map(int, input().split()))
count = [0] * (10 ** 5 + 5)
j = maxlen = unique = 0

for i in range(n):
    if count[a[i]] == 0:  # đếm số ptử phân biệt
        unique += 1
    count[a[i]] += 1

    # gặp ptử phân biệt thứ 3 => tiến hành thu gọn biên trái để tìm sang đoạn khác
    while j < n and unique > 2:
        if count[a[j]] == 1:  # chỉ có 1 ptử => loại nó khỏi unique luôn
            unique -= 1
        count[a[j]] -= 1
        j += 1

    # liên tục cập nhật
    maxlen = max(maxlen, i - j + 1)

print(maxlen)