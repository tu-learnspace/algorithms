# ctrl j -> hiển thị gợi ý main. c2: gõ main rồi ctrl+space
# ctrl alt l -> format code

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        if a[0] == 1:
            print('YES')
        else:
            print('NO')
    else:
        count = 0
        for i in range(n):
            if a[i] == 1:
                count += 1
        if count == n - 1:
            print('YES')
        else:
            print('NO')
