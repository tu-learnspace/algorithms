"""
https://codeforces.com/problemset/problem/242/B

- Gọi phân đoạn là [start, end] (end >= start). Cho các phân đoạn, hỏi phân đoạn nào bao trùm hết các phân đoạn còn lại
- Input:
    + dòng 1: chứa số phân đoạn
    + các dòng còn lại: mỗi dòng đại diện 1 phân đoạn, chứa 2 số start, end
- Output:
    + có phân đoạn bao trùm hết thì in ra phân đoạn thứ mấy, else -1
IDEA:
- Phân đoạn bao trùm hết là phân đoạn [a,b] với a là min, b là max trong tập hợp
- Cho tất cả giá trị start, end vô 1 list (sẽ có dạng [start1, end1, start2, end2, ...]). Tìm max, min
- Chỉ xét giá trị ở vị trí chẵn (start): nếu start = min -> xét thằng kế bên coi là max ko. Có thì xong bài
"""

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.extend(list(map(int,input().split())))

    na = len(a)

    max_value = max(a)
    max_index = a.index(max_value)
    min_value = min(a)
    min_index = a.index(min_value)
    pos = -1

    for i in range(0,na,2):
        if a[i] == min_value:
            if a[i+1] == max_value:
                pos = int(i/2 + 1)

    print(pos)

