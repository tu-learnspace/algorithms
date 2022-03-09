"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3359

- Dân số là p người (person), c là lệnh (command)
- Mỗi người dân mang ID từ 1 -> p, bệnh viện sẽ xử lý theo ưu tiên ID tăng dần (1->2->...->p)
- Sau khi xử lý 1 người xong thì người đó quay ra cuối hàng đợi
- Nếu có người cần được ưu tiên thì sẽ xử lý người đó trước
    + vd đang bth thì A ưu tiên, rồi B ưu tiên, rồi C ưu tiên thì xử lý C -> B -> A

- Input:
    + Dòng 1: p - dân số, c-số lệnh thực hiện
- Output: các dòng lệnh
    + Lệnh N là in ra người tiếp theo
    + Lệnh E x (x là người ưu tiên): đưa người x lên ưu tiên chứ ko in

IDEA:
- Ý tưởng cơ bản:
    + Khi gặp lệnh N thì in ra người ở top (queue-FIFO), sau đó put về cuối queue
    + Khi gặp lệnh E x thì đưa người x lên top
- Có thể thấy số p có thể rất lớn so với c (vd p = 10^5, c = 6) -> ko nhất thiết tạo queue cho p người
- Xét 2 TH:
    + Nếu c >= p: số lệnh nhiều hơn số người -> làm như ý tưởng cơ bản vì mảng người sẽ được duyệt qua hết
    + Nếu c < p: số người nhiều hơn số lệnh:
        - Thấy đc rằng số người nhiều đến bao nhiêu thì cũng chỉ thực hiện đủ c lệnh thôi.
        - Vẫn làm theo ý tưởng cơ bản, nhưng thật chất print actual queue thì thấy nó sai bét. Nhưng vẫn an toàn vì:
            + vd p=9, c=4 [1 2 3 4] 5 6 7 8 9 thì dù có full lệnh N thì cũng chỉ in tới người thứ 4 thôi, ko bao h đụng đc người 5
            => nghĩa là ko nhất thiết phải put 1 về sau 9, mà put 1 về sau 4 cũng đc
    => Chỉ tạo queue = min (c,p)
- Cách đưa người x lên top:
    + put x vào cuối queue.
    + lần lựa pop top queue ra rồi put vào cuối queue. Nếu gặp x thì bỏ qua. (lặp đủ size - 1 lần: -1 là do bỏ 1 lần bỏ qua x)
"""

from queue import Queue

def make_on_top(que, x):
    que.put(x)
    cnt = que.qsize() - 1
    while cnt > 0:
        value = que.get()
        if value != x:
            que.put(value)
        cnt -= 1

case = 1
while 1:
    p, c = map(int, input().split())
    if p == 0 and c == 0:
        break

    print('Case', case, end='')
    print(':')
    case += 1

    q = Queue()
    q_cnt = min(c, p)
    for i in range(q_cnt):
        q.put(i+1)

    for i in range(c):
        N = input()

        if N == 'N':
            value = q.get()
            print(value)
            q.put(value)
            # print('actual queue:', list(q.queue))
        else:
            x = int(N.split()[1])
            make_on_top(q, x)



