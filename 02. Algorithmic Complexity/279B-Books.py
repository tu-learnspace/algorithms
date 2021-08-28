"""
https://codeforces.com/problemset/problem/279/B

Có 1 lượng số phút rảnh.
Có 1 lượng sách, một lần đọc là đọc từ cuốn i -> i+1 -> i+2 -> ...
Mỗi lần đọc là phải đọc hết 1 cuốn.

- Input:
    + dòng 1: N số sách, T số phút rảnh
    + dòng 2: A1 A2 A3 ... An số phút cần để đọc hết cuốn thứ i
- Output: số lượng sách tối đa có thể đọc.

IDEA:
- Chọn ra đoạn nhiều sách LIÊN TIẾP nhất mà tổng thời gian đọc các quyển đó ko đc vượt giới hạn
+ ý tưởng thơ ngây:
    - cho start bđ, rồi cho end chạy từ start đến hết phần còn lại (khi nào vượt quá số phút cho phép thì dừng)
    - tăng start lên 1, rồi cũng cho end chạy như z
    - so sánh cái nào max nhất mà vẫn thỏa là oke
    => độ phức tạp O(N^2)
+ ý tưởng two pointer:
    - khi tìm đuọc vị trí đầu tiên bị > T là vị trí x (tức là đoạn x-1 trở về trc thỏa)  [x-? ... x-1] x
    - bỏ ptử đầu đoạn (x-?) thay bằng x, xem coi <= T chưa                              x-? [x-?+1 ... x]
    - nếu ko thì tiếp tục thu gọn cái đoạn đó                                     x-? x-?+1 [x-?+2 ... x]
    - nếu thỏa đk với T rồi (nhớ lưu lại để tìm max) thì ta lại tiếp tục tăng x bth và lặp lại như trên
    -> phát hiện đc tất cả các đoạn thỏa (nhờ đk đoạn là LIÊN TIẾP của đề nên chắc chắn ko sót) và tìm đc đoạn dài nhất.

"""
n, t = map(int, input().split())
a = list(map(int, input().split()))

read_time = 0
start_book = max_book = 0

for end_book in range(n):
    read_time += a[end_book]

    while read_time > t:
        read_time -= a[start_book]
        start_book += 1

    max_book = max(max_book, end_book - start_book + 1)

print(max_book)



