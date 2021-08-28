"""
https://www.spoj.com/problems/ONP/

- Đổi biểu thức đại số thành ký pháp Ba Lan ngược (RPN - Reverse Polish Notation)

- Input:
    + dòng 1: số lượng biểu thức
    + dòng 2: các biểu thức cần chuyển đổi

"""


def transform(exps):
    s = []
    for symbol in exps:
        if symbol.isalpha():
            print(symbol, end='')
        elif symbol == ')':
            print(s.pop(), end='')
        elif symbol != '(':
            s.append(symbol)
    print()


t = int(input())
for i in range(t):
    expression = input()
    transform(expression)
