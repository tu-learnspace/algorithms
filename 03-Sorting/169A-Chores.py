"""
https://codeforces.com/problemset/problem/169/A

- anh và em làm việc
- anh làm việc khó hơn em, tức là làm những việc có độ phức tạp > x, em thì làm cv có độ phức tạp <= x
- hỏi có bao nhiêu cách chọn x sao cho anh là đúng a công việc, em làm đúng b công việc

- Input:
    + dòng 1: n,a,b : tổng số công việc, số công việc anh, số công việc em (a+b=n)
    + dòng 2: chuỗi h là độ phức tạp công việc tương ứng.
- Output:
    + số cách chọn x. nếu ko có cách chọn thì in ra 0

IDEA:
    + em làm công việc trong khoảng h[0...n], anh làm trong khoảng [m ... end]
    + x sẽ là những số trong khoảng từ [n,m)
    + nếu m = n thì end
"""

n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

start = b-1
end = len(h)-a

solution = 0
if h[end] > h[start]:
    solution = h[end] - h[start]

print(solution)
