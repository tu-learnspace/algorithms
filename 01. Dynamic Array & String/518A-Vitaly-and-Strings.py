"""
https://codeforces.com/problemset/problem/518/A

- Input: 2 xâu cùng độ dài
    + dòng 1, xâu S.
    + dòng 2, xâu T (T>S)
- Ouput: Print ra xâu ở giữa S & T (T > res > S) hoặc 'No such string'

IDEA:
- Tìm chuỗi lớn hơn S theo thứ tự tiếp theo. So sánh nếu nhỏ hơn T thì ok.
- Quy tắc: chỉ cần +1 vô char cuối cùng -> lặp từ cuối lên, +1 char cuối rồi break
- Upper bound: z. Nếu chữ cuối là z thì đổi thành 'a' và chỉ +1 cho char kế bên (dez -> dfa)

VD:
    S = k
    T = m
    -> in ra: l

    S = klmnopq
    T = klmpopq
    -> in ra: klmnopr

    S = abcde
    T = abcdf
    -> in ra: no such string

Note: trong python string is immutable -> convert nó thành list, coi mỗi ptử trong list như char, cuối cùng join lại
"""
if __name__ == '__main__':
    s = input()
    t = input()
    n = len(s)
    res = list(s)

    for i in range(n - 1, -1, -1):
        if s[i] == 'z':
            res[i] = 'a'
        else:
            res[i] = chr(ord(s[i]) + 1)
            break

    res = "".join(res)

    if res < t:
        print(res)
    else:
        print('No such string')




