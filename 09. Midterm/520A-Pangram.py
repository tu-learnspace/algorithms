def get_char(c):
    if ord(c) > 96:
        return ord(c)
    else:
        return ord(c) + 32


n = int(input())
a = input()
c = []
for i in range(n):
    c.append(get_char(a[i]))

c.sort()
cnt = 0
for i in range(len(c)-1):
    if c[i] != c[i+1]:
        cnt += 1

if cnt == 25:
    print('YES')
else:
    print('NO')




