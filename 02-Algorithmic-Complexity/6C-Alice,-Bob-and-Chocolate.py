"""
https://codeforces.com/problemset/problem/6/C

- Có n thanh socola. Alice ăn từ trái sang phải và Bob ăn hướng ngược lại
- Với mỗi thanh socola, cần có tgian để ăn
- Tại mỗi thời điểm chỉ đc ăn 1 thanh, rồi move tới thanh tiếp theo
- Bob sẽ nhường Alice ăn thanh socola nếu gặp 1 thanh tại cùng thời điểm

- Input:
    + Dòng 1: N-số thanh socola
    + Dòng 2: dãy ti là thời gian ăn thanh socola thứ i
- Ouput:
    + 1 dòng gồm a-số thanh Alice ăn, b-sô thanh Bob ăn

IDEA:
- Dùng 2 con trỏ xét ở đầu mảng và cuối mảng
- Nếu tgian ăn của cả 2 như nhau -> alice ăn
=> cứ cho alice ăn, khi nào alice bận ăn thì bob mới đc ăn
"""
n = int(input())
t = list(map(int, input().split()))

i, j = 0, n-1
alice = bob = 0

while i <= j:
    if alice + t[i] <= bob + t[j]:  # alice sẽ hoàn thành trc bob nên bob phải nhường đén khi else
        alice += t[i]
        i += 1
    else:                           # alice đang ăn nên bob ko cần nhường
        bob += t[j]
        j -= 1

print(i, n-i)

