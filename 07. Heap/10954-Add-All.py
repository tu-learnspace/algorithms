"""
https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1895

- có nhiều thứ tự để cộng các số lại với nhau
- mỗi lần cộng 2 số thì chi phí bằng tổng 2 số đó
- tìm thứ tự cộng sao cho chi phí nhỏ nhất, tìm chi phí đó

- input: nhiều testcase. mỗi testcase:
    + dòng 1: N-kích thước của tập hợp số cần cộng
    + dòng 2: N số nguyên dương
- output: chi phí nhỏ nhất của mỗi testcase

IDEA:
- vd xét 3 số 1,2,3. có 3 cách cộng:
    + cộng 1,2 rồi cộng 3   => chi phí: 3 + 6 = 9
    + cộng 1,3 rồi cộng 2   => chi phí: 4 + 6 = 10
    + cộng 2,3 rồi cộng 1   => chi phí: 5 + 6 = 11
    => nhận xét: để cost min đc thì 2 số đc cộng luôn phải là 2 số nhỏ nhất
=> sử dụng min heap để lần lượt pop 2 số đầu rồi cộng => 2 số đc cộng luôn luôn chắc chắn nhỏ nhất
- sau khi cộng xong thì phải push tổng vào heap rồi làm tiếp (vì có thể tổng cộng lại sẽ lớn hơn số khác trong dãy thì ưu tiên cộng các số nhỏ trong dãy trc)

- useful testcase:
6
1 2 3 4 5 6
0
=> output: 51
"""
import heapq
h = []

while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    for x in a:
        heapq.heappush(h, x)

    cost = sum = 0
    while True:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        sum = a + b
        cost += sum
        if len(h) == 0:
            break
        heapq.heappush(h, sum)

    print(cost)

