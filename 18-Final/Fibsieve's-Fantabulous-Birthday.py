"""
https://lightoj.com/problem/fibsieves-fantabulous-birthday

- ma trận có mỗi ô đại diện 1 bóng đèn
- bóng đèn phát sáng theo thứ tự như hình
- cho 1 mốc thời gian, in ra cột, dòng của bóng đèn sẽ sáng vào thời điểm đó

IDEA:
- xem mốc thời gian ô đó phát sáng đại diện cho ô đó
- đề ko cho trc kích thước bàn cờ => phải dựa vào time (mốc thời gian) để tạo ra bàn cờ vừa đủ
- tìm bàn cờ n*n => lấy căn time làm tròn = n
=> ta luôn chọn bàn cờ n*n vừa khít nhất
=> ô cần tìm luôn nằm 1 trong 2 cạnh ngoài rìa (vòng bọc bên ngoài - chữ L ngược)

- xác định ô time cần chọn nằm ở cạnh nào. Vd cụ thể xét thời điểm 6:
    + n*n - time < n  => ở cạnh ngang trên
                      => x = n
                      => y = (n*n - time) + 1
    + n*n - time >= n => ở cạnh dọc phải
                      => y = n
                      - nhận thấy nếu rơi vào TH này thì chênh lệch (n*n - time) >= n
                      - 1 lần n là cạnh ngang, 1 lần n là cạnh dọc, để tìm độ chênh lệch (cũng là x) => lấy 2*n trừ
                      => x = (2*n - chênh lệch) - 1

- tuy nhiên mỗi vòng bọc bên ngoài mới (chữ L ngược mới) => công thức tính x, y bị đảo ngược
(vd xét thời điểm 15 & thời điểm 6 kế bên trong ma trận nhưng công thức tính x, y bị đảo)
=> check vòng đó là chẵn hay lẻ mà đảo công thức
"""
import math

tc = int(input())
for i in range(tc):
    time = int(input())

    # tìm n
    n = math.ceil(math.sqrt(time))

    x = y = -1      # dòng, cột

    if n * n - time < n:
        x = n
        y = n * n - time + 1
    else:
        y = n
        x = 2 * n - (n * n - time) - 1

    # công thức sẽ bị đảo ngược với từng vòng bọc bên ngoài
    if n % 2 != 0:
        x, y = y, x

    print('Case {}: {} {}'.format(i + 1, x, y))
