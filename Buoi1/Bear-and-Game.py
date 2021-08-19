'''
https://codeforces.com/problemset/problem/673/A
- Một trận đấu dài 90 phút.
- Nếu 15 phút liên tiếp boring thì tắt TV -> phút 16
- Biết đc phút thứ N interesting -> tính số thời gian xem TV.
- Input:
    + dòng 1: số lượng phút interesting
    + dòng 2: danh sách phút interesting
- Output: số phút coi.

IDEA:
- 2 khoảng interesting lớn >= 15 -> boring enough to off
'''

if __name__ == '__main__':
    n = int(input())
    t = list(map(int, input().split()))

    T = 0

    if n == 1 and t[0] <= 15:
        watched = t[0] + 15
    elif t[0] >= 16:
        watched = 15
    else:
        for i in range(n - 1):
            if t[i] - T > 15:
                T += 15
                break
            else:
                T = t[i]

        if T > 90:
            T = 90
        else:
            T += 15

    print(watched)
