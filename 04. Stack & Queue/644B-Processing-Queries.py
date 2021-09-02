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

"""
from queue import Queue
class Query:
    def __init__(self, t, d, id):
        self.t = t
        self.d = d
        self.id = id

n, b = map(int, input().split())

q = Queue()
complete_time = 0
ans = [0]*n

for i in range(n):
    t, d = map(int, input().split())
    query = Query(t, d, i)

    if complete_time < t:
        while q.qsize():
            job = q.get()
            complete_time = max(complete_time,job.t) + job.d
            ans[job.id] = complete_time
            if complete_time > t:
                break

    if complete_time > t:
        if q.qsize() < b:  # queue still enough
            q.put(query)
        else:  # queue is full
            ans[i] = -1
            break
    else:
        complete_time = max(complete_time, t) + d
        ans[i] = complete_time

while q.qsize():
    job = q.get()
    complete_time = max(complete_time,job.t) + job.d
    ans[job.id] = complete_time


for i in range(len(ans)):
    print(ans[i], end=' ')