"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1876

- Có xấp bài
- Lá trên cùng sẽ đc rút ra rồi giục vô thùng rác
- Lá trên cùng mới sau thao tác này (tức là lá tiếp theo lúc chưa giục) sẽ được chuyển xuống dưới đáy.
- Tìm ra thứ tự các lá bài sẽ được rút ra, cũng như lá cuối cùng còn sót lại.

- Input:
    + nhiều dòng, mỗi dòng là 1 test case. kết thúc là 0
- Output:
    + Discarded cards và Remaining card của từng test case

IDEA:
- Xài 1 cái queue bình thường
- khi giục rác thì là pop top ra rồi in.
- lá tiếp theo xuống cuối -> pop top ra rồi put vô cuối queue
"""
from queue import Queue

while 1:
    n = int(input())
    if n == 0:
        break

    q = Queue()
    for i in range(1, n + 1, 1):
        q.put(i)

    if q.qsize() == 1:
        print('Discarded cards:', end='')
    else:
        print('Discarded cards: ', end='')

    while q.qsize() != 1:
        if q.qsize() == 2:
            print(q.get(), end='')
        else:
            print(q.get(), end=', ')
        value = q.get()
        q.put(value)
    print("\nRemaining card:", q.queue[0])
