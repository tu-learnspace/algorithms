"""
https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/

- cho một dãy số A, i chạy từ 1 đến N
- tính tích của số lớn nhất, số lớn thứ hai và số lớn thứ ba của đoạn con từ 1 đến i
- hai phần tử cùng giá trị nhưng có chỉ số khác nhau vẫn được tính là khác nhau

- input:
    + dòng 1: N- số ptử dãy
    + dòng 2: N số nguyên biểu diễn dãy
- output: với mỗi i, in ra kết quả, nếu k có ptử lớn t2, t3 thì in -1

IDEA:
- c1: tạo mảng rồi sort rồi xét 3 phần tử lớn nhất nhân lại
- c2: tạo 1 cái max-heap. luôn lấy đc ptử lớn nhất bằng cách pop gốc ra
"""
import heapq
class PQEntry:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other):
        return self.value > other.value


n = int(input())
a = map(int, input().split())
h = []

for x in a:
    heapq.heappush(h, PQEntry(x))

    if len(h) < 3:
        print(-1)
    else:
        temp = []
        res = 1
        # pop 3 top elements
        for _ in range(3):
            top = heapq.heappop(h)
            res *= top.value
            temp.append(top.value)
        # push them back
        for i in temp:
            heapq.heappush(h, PQEntry(i))

        print(res)