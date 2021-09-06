"""
https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/

- Cho số X và Y. Và một dãy số Ai. Có thể nhân Ai như thế nào vào X để được Y không? (mỗi số chỉ nhân 1 lần, nhân liên tiếp vô tích đã nhân)
- Thời gian cho 1 phép nhân là 1s. Tính tổng thời gian để nhân X thành Y

- Input:
    + Dòng 1: X và Y
    + Dòng 2: N-kích thước mảng Ai
    + Dòng 3: N số nguyên đại diện Ai
- Output: thời gian để nhân. Không được thì print -1

IDEA:
- X là node bắt đầu
- tìm bfs tới node cuối cùng là Y
- mở rộng grap bằng những node tiếp theo là (X * Ai) % 10^5
- thời gian cho 1 phép nhân = 1s => tổng thời gian = khoảng cách từ X tới Y

"""
from queue import Queue

MAX = 10 ** 5 + 5


def BFS(my_key, bank_key, keys, dist):
    q.put(my_key)
    dist[my_key] = 0

    while not q.empty():
        temp = q.get()
        if temp == bank_key:
            break
        for i in range(len(keys)):
            next = (temp * keys[i]) % 100000

            if next == bank_key:
                print(dist[temp] + 1)
                exit()

            if dist[next] == -1:
                dist[next] = dist[temp] + 1
                q.put(next)

    print(dist[bank_key])


if __name__ == '__main__':
    q = Queue()
    dist = [-1 for _ in range(MAX)]

    my_key, bank_key = map(int, input().split())
    key_num = int(input())
    keys = list(map(int, input().split()))
    BFS(my_key, bank_key, keys, dist)


