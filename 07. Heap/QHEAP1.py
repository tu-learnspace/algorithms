"""
https://www.hackerrank.com/challenges/qheap1/problem

- Có các truy vấn:
    - "1 v”: thêm một phần tử vào heap
    - “2 v”: xóa một phần từ của heap
    - “3”: in ra phần tử có giá trị nhỏ nhất trong các phần tử của heap
- đảm bảo ptử đc xóa có trong heap & trong heap chỉ có ptử riêng biệt

- input:
    + dòng 1: Q-số lượng truy vấn
    + mỗi dòng tiếp theo là 1 trong 3 loại truy vấn trên
- output: với mỗi truy vấn loại 3, in ra một dòng duy nhất chứa giá trị nhỏ nhất

IDEA:
- sử dụng min-heap
- khi xóa 1 ptử bất kỳ thì pop tới khi nào gặp ptử đó thì put lại các ptử đã pop vô => có thể bị TLE
=> ko cần thật sự xóa ptử đó. vì nếu mình chỉ cần pop top ra thôi thì ptử khác có bị xóa hay ko cũng ko quan trọng
=> dùng dict để lưu lại ptử nào đã bị xóa (chứ k thực sự xóa nó)
- khi pop top thì xem coi đã bị xóa chưa, nếu rồi thì cứ pop đến khi nào tới ptử chưa bị xóa
"""
import heapq
h = []

n = int(input())
deleted = dict()

for _ in range(n):
    q = list(map(int, input().split()))

    if q[0] == 1:
        heapq.heappush(h, q[1])
        deleted[q[1]] = False
    elif q[0] == 2:
        deleted[q[1]] = True
    else:
        while deleted[h[0]] == True:
            heapq.heappop(h)
        print(h[0])