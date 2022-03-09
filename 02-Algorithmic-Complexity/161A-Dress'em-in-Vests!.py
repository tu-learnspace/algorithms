"""
https://codeforces.com/problemset/problem/161/A

- Vương quốc có N chiến binh
- Chiến binh thứ i đăng ký áo giáp cỡ phù hợp Ai
- Tất cả chiến binh vẫn có thể mặc giáp trong khoảng [Ai-X, Ai+Y]
- Vương quốc đã có M bộ giáp với kích cỡ B
- Hỏi làm sao để phân chia lượng áo giáp cho nhiều chiến binh nhất có thể (mỗi chiến binh 1 áo giáp)

- Input:
    + Dòng 1: N-số lg chiến binh, M-số lượng áo giáp, X,Y: khoảng chấp nhận đc
    + Dòng 2: chứa N số nguyên A1,A2,...An tăng dần: kích thước giáp chiến binh đăng ký
    + Dòng 3: chứa M số nguyến B1,B2,...Bn tăng dần: kích cỡ của các áo giáp hiện tại trong kho
- Output:
    + Dòng 1: K-số lg max chiến binh đc trang bị áo giáp
    + K dòng tiếp theo, mỗi dòng gồm cặp U, V: người lính U nhận được áo giáp thứ V

IDEA:
- Để có số lượng chiến binh đc mặc giáp tối ưu/lớn nhất => giáp bé nhất phải đc đưa cho ng mặc vừa bé nhất, dành giáp lớn cho ng sau
- Nhờ mảng A, B đã đc sắp xếp tăng dần như vậy thì khi vị trí i/j không thỏa
    => chắc chắn vị trí trước đó cũng ko thỏa. thoải mái tăng lên vị trí tiếp theo mà ko sợ bị sót TH
- Cho 2 con trỏ vào cặp lính-áo:
    + cái nào ko ổn thì + biến của cái đó lên (tới cái tiếp theo).
    + cả 2 đều ổn thì ++ cả 2 lên (tới cặp tiếp theo) vào append vô mảng ans

- Useful testcase:
    3 3 2 2
    1 5 9
    4 4 10
=>  2
    2 1
    3 3
"""
n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = []
i = j = 0

while i < n and j < m:
    if a[i] - x <= b[j] <= a[i] + y:
        j += 1
        i += 1
        ans.append((i, j))
    elif a[i] - x > b[j]:  # giáp b[j] quá nhỏ, phải xét giáp tiếp theo (chắc chắn giáp tiếp theo bự hơn)
        j += 1
    elif b[j] > a[i] + y:  # giáp b[j] quá lớn, phải xét ng tiếp theo vừa ko (vì chắc chắn ng tiếp theo sẽ đký size lớn hơn)
        i += 1

print(len(ans))
for a in ans:
    print(a[0], a[1])

