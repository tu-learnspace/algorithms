"""
https://codeforces.com/problemset/problem/439/B

- 1 môn học có nhiều chương, mỗi chương có x giờ học (trong 1 môn thì chương nào cũng có thời gian học như nhau).
- sau khi học xong một môn này thì môn sau có chương có số giờ học giảm đi 1 tiếng
- giờ học giảm đến tối thiểu 1 tiếng

- Input:
    + dòng 1: n: số môn, x: thời gian học 1 chương trong môn đầu tiên (mỗi môn sau giảm dần)
    + dòng 2: n số nguyên đại diện số chương của môn thứ i
- Output: thời gian tối thiểu để học xong môn.

IDEA:
- vì cứ xong 1 môn thì số giờ trong chương giảm 1, dù môn đó có bao nhiêu chương đi nữa
-> môn nào có ít chương học trước, môn nào có nhiều chương học sau (môn học sau đc hưởng lợi vì giở học giảm)
"""

n, x = map(int, input().split())
subjects = list(map(int, input().split()))

subjects.sort()
min_time = 0
for subject in subjects:
    min_time += subject * x
    if x > 1:
        x -= 1
print(min_time)
