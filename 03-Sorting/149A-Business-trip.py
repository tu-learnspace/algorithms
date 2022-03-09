"""
https://codeforces.com/problemset/problem/149/A

- cây được tưới vào tháng i thì cao thêm Ai cm
- cần phải chọn tháng tưới làm sao để cao ít nhất K cm (ko nhất thiết liên tục)

- Input:
    + dòng 1: số k (cây phải cao đến k cm)
    + dòng 2: mảng 12 ptử (đại diện 12 tháng), mỗi ptử thể hiện gtrị cây cao thêm bao nhiu nếu đc tưới trong tháng đó
- Output: số tháng ít nhầt cần tưới, ko đc thì -1

IDEA:
- sort theo thứ tự tăng dần, rồi bắt đầu cộng từ cuối mảng
    + vì ở đây ko bắt chỉ ra chính xác cộng lại bằng mà kêu chỉ ra số tối thiểu
    => đi từ cuối mảng (ptử lớn nhất) là tối ưu nhất (số tháng là ít nhất) rồi.
- THĐB, cả mảng ko thỏa nổi (số K quá lớn) => cuối cùng phải check coi có < hơn K ko, nếu có thì -1
"""

k = int(input())
a = list(map(int, input().split()))

a.sort()

crr = months = 0

if k == 0:
    print(0)
else:
    for i in range(len(a) - 1, -1, -1):
        if crr < k:
            crr += a[i]
            months += 1
        elif crr >= k:
            break
    if crr < k:
        months = -1

    print(months)
