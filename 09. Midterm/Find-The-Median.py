"""
https://www.hackerrank.com/challenges/find-the-median/problem

"""
n = int(input())
a = list(map(int, input().split()))

a.sort()
median = -1

if n % 2 != 0:
    median = a[n // 2]
else:
    a = a[n//2 - 1]
    b = a[n//2]
    median = (a+b) / 2

print(median)

