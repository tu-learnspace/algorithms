"""
https://codeforces.com/problemset/problem/721/B

- Nhập mật khẩu theo thứ tự sao cho không làm giảm độ dài của chúng và mật khẩu có cùng độ dài theo thứ tự tùy ý
- Không nhập bất kì mật khẩu nào 2 lần
- Mất 1s để nhập mật khẩu
- Nếu nhập sai mật khẩu k lần (khai báo trong input), thì thực hiện lần thử tiếp theo sau 5s

- Input:
    + dòng 1: n: số mật khẩu
    + dòng 2: k: số lần thủ ko thành công (sau k lần thì bị chặn 5s)
    + n dòng tiếp theo: chứa các mật khẩu
    + dòng cuối cùng: mật khẩu chính xác (giống 1 trong các mật khảu dòng trên)
- Output:
    + 2 số nguyên best & worst case
IDEA:
- chuỗi nhập theo tăng dần độ dài
- best case:
    + nếu tất cả chuỗi nhập có cùng độ dài -> best case = 1 (lần nhập đầu tiên)
    + nếu có chuỗi ko cùng -> best case: sau khi nhập hết chuỗi độ dài bé hơn
- worst case:
    + nhập hết các chuỗi bé hơn. rồi nhập các chuỗi bằng. (-1 vì trừ đi pass đúng)
- tgian:
    + tgian nhập: mỗi pass * 1 . tính xong thì nhớ +1 (vì nhập pass đúng tốn 1s).
    + tgian chờ: lấy floor(số pass phải nhập/k)* 5
"""

n, k = map(int, input().split())
cnt = [0]*101  # đếm số loại độ dài chuỗi

for i in range(n):
    s = input()
    cnt[len(s)] += 1

password = input()

best_case = worst_case = 0

# thời gian nhập pass
for pass_len in range(len(password)):
    best_case += cnt[pass_len]

worst_case = best_case + cnt[len(password)] - 1

# thời gian bị phạt
best_case += (best_case//k)*5 + 1
worst_case += (worst_case//k)*5 + 1

print(best_case, worst_case)