"""
https://www.spoj.com/problems/STPAR/

- Cần 1 đoàn diễu hành phải theo thứ tự 1, 2, 3, ..., n
- Vì đời ko như là mơ, đoàn diễu hành ko có theo thứ tự như z. Cho nên có 1 con đường tạm, cho xe nào sai thứ tự thì đi vào đó chờ tạm, nhường xe khác đi.
- Xe không được đi lùi (coi hình minh họa cho dễ hiểu)

- Input:
    + lưu ý input ở đây có nhiều TH, kết thúc toàn bộ bài bằng số 0. vd:
        n1
        TH1
        n2
        TH2
        ...
        0
- Ouput: 1 loạt dòng yes hoặc no vs mỗi TH.

IDEA:
- Sử dụng 2 stack (thật ra khi code chỉ cần 1):
    + 1 stack chứa phẩn tử tiếp theo cần tìm (thật ra ko cần implement thằng này, xài để check thui)
    + 1 stack tạm để chứa mấy đứa tùm lum ko theo thứ tự
- Check điều kiện coi:
    + thỏa thì push vô stack chính (thật ra ko cần implement thằng này, xài để check thui)
    + ko thỏa thì tạm cho vào stack temp:
    + sau 2 bước trên thì kiểm tra coi top của stack temp có ptử cần tìm ko, nếu có thì pop ra.
=> nếu ptử đỉnh stack temp nhỏ hơn ptử đỉnh stack chính (find) thì sẽ k thể sắp xếp được đoàn xe này nữa.

- Useful test-case:
10
1 2 10 5 4 3 9 8 7 6
0
"""

while 1:
    n = int(input())
    if n == 0:
        break
    cars = list(map(int, input().split()))

    # s = []
    temp = []
    find = 1

    for i in range(n):
        # push những ptử ko theo thứ tự vào stack tạm
        if cars[i] == find:
            # s.append(cars[i])
            find += 1
        else:
            temp.append(cars[i])

        # kiểm tra đỉnh stack tạm có phải là ptử cần tìm ko -> có thì pop ra
        if len(temp) != 0:
            while temp[-1] == find:
                value = temp.pop()
                # s.append(value)
                find += 1

                if len(temp) == 0:
                    break

    # ko còn thằng nào trong stack tạm nghĩa là ổn hết (mọi ptử đểu thỏa đk nên đi ra hết rồi)
    if len(temp) == 0:
        print("yes")
    else:
        print("no")


