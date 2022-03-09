"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=3146

- có 2 dạng truy vấn:
    + 1 x: thêm ptử x vào túi
    + 2 x: lấy ptử ra khỏi túi, giá trị lấy ra là x
- dựa vào các truy vấn đc thực hiện, đoán xem nó là queue, stack hay priority-queue (max-heap)

- input: nhiều testcase, mỗi testcase có:
    + dòng 1: số truy vấn
    + các dòng sau: các truy vấn
- output: với mỗi testcase in ra loại cấu trúc dữ liệu đó, nếu ko chắc thì in not sure, ko thể thì impossible

IDEA:
- sử dụng ctdl đó luôn để ktra => nếu lúc pop ra mà ko giống thì check ctdl đó là false
- not sure nghĩa là có tính chất của ít nhất 2 cái
- khi push hoặc pop thì check vẫn còn thỏa tính chất thì mới thực hiện
"""
import heapq
from queue import Queue

try:
    while True:
        s = h = []
        q = Queue()

        is_stack = is_queue = is_heap = True

        n = int(input())
        for _ in range(n):
            u, v = map(int, input().split())

            if u == 1:
                if is_stack:
                    s.append(v)
                if is_queue:
                    q.put(v)
                if is_heap:
                    heapq.heappush(h, -v)
            else:
                if is_stack:
                    if v != s[-1]:
                        is_stack = False
                    else:
                        s.pop()
                if is_queue:
                    if v != q.queue[0]:
                        is_queue = False
                    else:
                        q.get()
                if is_heap:
                    if -v != h[0]:
                        is_heap = False
                    else:
                        heapq.heappop(h)

        if is_stack and not is_queue and not is_heap:
            print('stack')
        elif is_queue and not is_stack and not is_heap:
            print('queue')
        elif is_heap and not is_stack and not is_queue:
            print('priority queue')
        elif not is_stack and not is_queue and not is_heap:
            print('impossible')
        else:
            print('not sure')

except EOFError:
    pass



