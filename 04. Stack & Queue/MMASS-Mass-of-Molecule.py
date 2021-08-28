"""
https://www.spoj.com/problems/MMASS/

- Công thức hóa học bao gồm C, H, O

- Input: công thức
- Output: khối lượng M của công thức

IDEA:
- Sử dụng stack
- Gặp '(': push vào stack (push -1 đại diện)
- Gặp nguyên tố (C,H,O): push M của nó vào
- Gặp số: pop đỉnh stack ra nhân với số rồi push vô lại
- Gặp ')': pop tất cả số trước '(' rồi cộng lại rồi push lại vào stack
- Cuối cùng cộng tất cả các số trong stack -> mass
"""

def getMole(c):
    if c == 'C':
        return 12
    elif c == 'H':
        return 1
    elif c == 'O':
        return 16

formula = input()
s = []
for c in formula:
    if c == '(':
        s.append(-1)
    elif c == ')':
        sm = 0
        while len(s) > 0 and s[-1] != -1:
            sm += s.pop()
        s.pop()  # pop '('
        s.append(sm)
    elif c.isalpha():
        s.append(getMole(c))
    elif c.isdigit():
        sm = int(c) * s.pop()
        s.append(sm)

mass = 0
while len(s) > 0:
    mass += s.pop()
print(mass)
