"""
https://codeforces.com/problemset/problem/387/B

- Geogre đã chuẩn bị M bài toán , mỗi bài có độ phức tạp Bi
- Để có vòng thi tốt, phải giải ít nhất N đề thi. Cần phải có ít nhất 1 bài toán vs độ phức tạp A1, A2,...An
- Với bài toán có độ phức tạp C thì Geogre có thể biến nó thành độ phức tạp D (D < C)
- Cần tìm ra số lượng bài toán tối thiểu cần phải giải quyết ngoài M bài toán đã đặt ra để có thể vượt qua tốt vòng thi

- Input:
    + dòng 1: N-số bài toàn tối thiểu của vòng thi tốt; M-số bài toán đã chuẩn bị
    + dòng 2: các số A1 ... An là yêu cầu về độ phức tạp bài toán của vòng thi tốt (theo thứ tự tăng dần)
    + dòng 3: các số B1 ... Bn là độ phức tạp bài toán đã chuẩn bị (theo tứ tự tăng dần)
- Output: in ra đáp án bài toán
- VD:
    + đề thi: 1 2 3
    + đã chuẩn bị: 1 1 1 1 1
    => cần chuẩn bị thêm bài toán có độ phức tạp 2, 3 là đủ pass vòng thi

IDEA:
- Nôm na là cho dãy A và dãy B, mỗi ptử của B phải ứng với mỗi ptử của A sao cho (Bi >= Ai), tìm xem có bao nhiu Ai ko thể có cái khớp
- Cho dễ hiểu, xem bài chuẩn bị là bài giải, bài giải phải có độ khó ít nhất = đề thi thì mới giải đc
    => Nếu có nhiều bài giải có thể giải đc thì lấy bài có độ phức tạp nhỏ nhất (đề dành lớn hơn cho mấy cái sau)
- Nếu xét tới đề thi độ khó thứ i mà ko có bài giải đc
    => đề thi độ khó thứ i+1 cũng ko có bài giải đc luôn
- Note thêm làm sao biết là ko còn cách nào trc đó phù hợp: Nếu đã chọn bài giải thứ j cho đề thi i
    => Khi xét đề thi tiếp theo i+1 thì bài giải trc bài j ko thể sử dụng đc (vì idea 1 đã chọn độ phức tạp nhỏ nhất)

"""

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0  # số đè thi đã tìm đc lời giải phù hợp
i = 0

for j in range(m):
    if i >= n:
        break

    if b[j] >= a[i]:
        i += 1
        count += 1

print(n - count)
