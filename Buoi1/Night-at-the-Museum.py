"""
Cho 1 vòng tròn chữ cái, kiểu như quay số điện thoại ngày xưa (ngoại trừ nó ko tự quay lại vị trí ban đầu)
Input là 1 string
Output là số nhỏ nhất tổng các vòng xoay để in ra string đó


"""

if __name__ == '__main__':
    name = input()
    chars = [char for char in name]

    count = 0
    pos = 0

    for char in chars:

