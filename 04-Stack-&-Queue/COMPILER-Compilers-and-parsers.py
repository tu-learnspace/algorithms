"""
https://www.codechef.com/problems/COMPILER

- câu lệnh hợp lệ:
    + < < > > < < > > : max len = 4
    + < > < > : max len = 2
    + < > < > < > < > : max len = 2
    + < > > > : max len = 2
- không hợp lệ:
    + > > > >
    + > < > < > < > <

- Input:
    + dòng 1: số test case
    + mỗi dòng tiếp theo: xâu T
- Output:
    + mỗi dòng ứng với độ dài tiền tố lớn nhất hợp lệ của T hoặc 0 nếu ko hợp lệ

IDEA:
- Có mở thì phải có đóng, có thể dư '>' đằng sau nhưng ko đc dư '<'
- Bắt đầu với > thì ko hợp lệ
- Một dấu < tương ứng với 1 dấu >
=> cứ 1 dấu < thì push vô stack, 1 dấu > thì pop ra stack:
    + nếu stack empty nghĩa là mọi dấu < đã đc đóng hợp lệ => max = số lần lặp để đóng thành công hết
    + cần check nếu bắt đầu bằng < (len = 0 mà lại pop)

- Useful test-case:
< < > < < >
"""

n = int(input())
for i in range(n):
    s = []
    instruction = input()
    max_len = 0
    cnt = 0

    for char in instruction:
        cnt += 1
        if char == '<':
            s.append(1)
        elif char == '>':
            if len(s):
                s.pop()
            else:  # start with '>' => false
                break
        if len(s) == 0:  # empty mean all the < has the close >
            max_len = cnt

    print(max_len)

