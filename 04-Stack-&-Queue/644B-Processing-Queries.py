"""
https://codeforces.com/problemset/problem/644/B

- Khi một truy vấn xuất hiện, máy chủ sẽ phản hồi theo ba cách:
    + Nếu máy chủ đang trống và hàng đợi truy vấn đang trống thì máy chủ sẽ ngay lập tức xử lí truy vấn này.
    + Nếu máy chủ đang bận xử lí và hàng đợi truy vấn đang có ít hơn B truy vấn thì truy vấn mới sẽ được thêm vào cuối hàng đợi.
    + Nếu máy chủ đang bận xử lí và hàng đợi truy vấn đã có đủ B truy vấn thì truy vấn mới sẽ bị từ chối và sẽ không bao giờ được xử lí.

- Input:
    + dòng 1: N-số truy vấn, B-max của hàng dợi
    + N dòng tiếp theo thứ tự thời gian gồm 2 số: số phút và thời gian xử lý của truy vấn đó.
- Output:
    + in ra thời điểm hoàn thành xử lý truy vấn đó, bị từ chối thì -1

IDEA:
- Khởi tạo hàng đợi, đẩy truy vấn vào hàng đợi. Ta chỉ lưu thời gian cần để xử lý xong truy vấn.
- Khi mà hàng đợi còn chỗ, ta push thời gian xử lý xong truy vấn đó vào. Nếu hết chỗ thì từ chối (print -1)
- t là thời điểm mà ta đang xét:
    + thời điểm đó lớn hơn thời gian làm xong truy vấn first in có trong queue => pop nó ra
"""
from queue import Queue

n, b = map(int, input().split())
q = Queue()
process_time = 0

for i in range(n):
    t, d = map(int, input().split())

    while q.qsize() != 0 and t >= q.queue[0]:
        q.get()   # thời điểm hiện tại đang xét > thời gian xử lý xong truy vấn first in => nó đã làm xong, pop nó ra

    if q.qsize() <= b:  # hàng đợi còn chỗ (push vào tối đa b + 1 job), vì giả sử cái job đang trong queue đang đc làm => thật ra queue vẫn còn trống 1 chỗ)
        process_time = max(t, process_time) + d
        q.put(process_time)
        print(process_time, end=' ')
    else:               # hết chỗ nên từ chối
        print(-1, end=' ')
