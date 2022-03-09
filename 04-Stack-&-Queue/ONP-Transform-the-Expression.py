"""
https://www.spoj.com/problems/ONP/

- Đổi biểu thức đại số thành ký pháp Ba Lan ngược (RPN - Reverse Polish Notation)

- Input:
    + dòng 1: số lượng biểu thức
    + dòng 2: các biểu thức cần chuyển đổi
- Ouput:
    + các dòng tương ứng ký pháp Ba Lan ngược của biểu thức cần đổi.

IDEA:
- Phân tích thấy: dấu ngoặc ko đc in ra mà để xử lý tính toán ưu tiên biểu thức nào
- Ưu tiên in các biến khi đã có đủ các cặp ngoặc rồi mới in phép toán
- Xét TH:
    + gặp dấu '(' thì bỏ qua. Ta hoàn toàn có thể bỏ qua vì đề bài cho 1 toán tử chỉ có 2 toán hạng, và ko có TH kiểu a*b*c (tức là (a*b)*c = a*(b*c) đều tồn tai)
    + nếu là chữ latin -> in ra luôn
    + nếu là phép toán -> bỏ vào stack
    + nếu là ')' -> dấu hiệu đã hết biểu thức '()' -> ta lấy toán tử từ stack ra rồi in
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
