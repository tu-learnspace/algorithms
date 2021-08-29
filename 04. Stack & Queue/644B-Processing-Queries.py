"""
https://codeforces.com/problemset/problem/644/B

- Khi một truy vấn xuất hiện, máy chủ sẽ phản hồi theo ba cách:
    + Nếu máy chủ đang trống và hàng đợi truy vấn đang trống thì máy chủ sẽ ngay lập tức xử lí truy vấn này.
    + Nếu máy chủ đang bận xử lí và hàng đợi truy vấn đang có ít hơn B truy vấn thì truy vấn mới sẽ được thêm vào cuối hàng đợi.
    + Nếu máy chủ đang bận xử lí và hàng đợi truy vấn đã có đủ B truy vấn thì truy vấn mới sẽ bị từ chối và sẽ không bao giờ được xử lí.

- Input:
    + dòng 1: N-số truy vấn, B-max của hàngd dợi
    + N dòng tiếp theo thứ tự thời gian gồm 2 số: số phút và thời gian xử lý của truy vấn đó.
- Output:
    + in ra thời điểm hoàn thành xử lý truy vấn đó, bị từ chối thì -1

IDEA:

"""

n, b = map(int, input().split())

for i in range(n):
    t, d = map(int, input().split())
