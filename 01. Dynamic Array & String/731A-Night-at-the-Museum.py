"""
https://codeforces.com/problemset/problem/731/A

- Cho 1 vòng tròn chữ cái, kiểu như quay số điện thoại ngày xưa (ngoại trừ nó ko tự quay lại vị trí ban đầu)
- Input là 1 string
- Output là số nhỏ nhất tổng các vòng xoay để in ra string đó
- Có 26 chữ cái, bắt đầu tại 'a'.

IDEA:
 - init tại pos = 'a'
 - tính l1 và l2 là khoảng cách giữa 'a' và chữ cái (từ 2 phía)
 - chọn min của l1,l2 rồi + vô count
 - cập nhật pos mới là vị trí chữ cái hiện tại
"""

if __name__ == '__main__':
    name = input()
    chars = [char for char in name]

    count = 0
    pos = 97  # init at 'a'

    for char in chars:
        l1 = abs(ord(char) - pos)
        l2 = 26 - l1
        l = min(l1, l2)
        count += l
        pos = ord(char)

    print(count)
