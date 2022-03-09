"""
https://codeforces.com/problemset/problem/471/B

- các công việc có độ ưu tiên khác nhau (cao nhất là 1 rồi độ ưu tiên giảm dần theo 2, 3, 4, ...)
- công việc có độ ưu tiên cao cần làm trước công việc có độ ưu tiên thấp
- cần in ra ba kế hoạch làm việc khác nhau

IDEA:
- vì đề bài cần in ra index của công việc => dùng tuple lưu trữ (độ_quan_trọng, index), có thể sort đc theo độ_quan_trọng
- các công việc có cùng độ ưu tiên có thể swap cho nhau để ra kế hoạch mới
- để in ra đc ba kế hoạch thì ít nhất phải có 2 cặp công việc có thể swap đc cho nhau
(plan 1: như bth, plan 2: sort 1 cặp nào đó, plan 3: sort 1 cặp khác)
"""

n = int(input())
h = list(map(int, input().split()))

d = []
for i in range(n):
    d.append((h[i], i + 1))

d.sort()

cnt = 0
for i in range(n - 1):
    if d[i][0] == d[i + 1][0]:          # độ quan trọng bằng nhau
        cnt += 1

    if cnt == 2:                        # ít nhất 2 cặp có thể swap đc là có thể in đc 3 plan
        print('YES')

        for j in range(n):              # plan đầu tiên: làm bth theo độ ưu tiên đc sort
            print(d[j][1], end=' ')
        print('')

        plan = 0
        for j in range(n):                          # in ra plan 2 & 3
            if d[j][0] == d[j + 1][0]:              # nếu 2 thằng có cùng độ ưu tiên
                d[j], d[j + 1] = d[j + 1], d[j]     # => swap 2 thằng này

                plan += 1
                for k in range(n):
                    print(d[k][1], end=' ')
                print('')

                d[j], d[j + 1] = d[j + 1], d[j]     # swap 2 thằng trên để trả lại bth

            if plan == 2:
                exit()

print('NO')
