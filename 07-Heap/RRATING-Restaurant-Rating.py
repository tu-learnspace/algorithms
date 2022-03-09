"""
https://www.codechef.com/problems/RRATING

- nhà hàng có các review
- Chef muốn chỉ hiển thị top 1/3 review tốt nhất về nhà hàng lên website
- Chef chỉ muốn xem bài review tệ nhất trong top 1/3 các bài review đó
- đề bài sẽ cho 1 loạt truy vấn:
    + 1 x: thêm bài review có số điểm x vào
    + 2: hiển thị review tệ nhất trên website

- input:
    + dòng 1: số lượng truy vấn
    + các dòng tiếp theo là truy vấn
- output: với mỗi truy vấn dạng 2, in ra bài review tệ nhất trên website, chưa có thì 'No reviews yet'

IDEA:
- maxheap để lưu tất cả review
- sử dụng 1 minheap để lưu top 1/3 review tốt nhất (review chỉ xuất hiện ở maxheap hoặc minheap)
=> muốn in review thấp nhất thì chỉ cần pop top của minheap đó ra
- nhận xét top 1/3: vd có 3 bài thì top có 1 bài, 6 bài thì top có 2 bài, 9 bài thì top có 3 bài
 => cứ thêm 3 bài mới thì số bài review top tăng 1
 => pop maxheap (best from all reviews) ra rồi push vào minheap (top review)
- khi push vào phải so sánh với ptử min hiện tại trong minheap:
    + nếu review mới nhỏ hơn thì pop minheap để thay thế
    + nếu review mới lớn hơn thì thôi để bth ko push
"""
import heapq
reviews = []    # max-heap
top_rev = []    # min-heap

class PQEntry:
    def __init__(self, review):
        self.review = review
    def __lt__(self, other):
        return self.review > other.review

n = int(input())
count = 0
for i in range(n):
    q = list(map(int, input().split()))

    if q[0] == 1:
        count += 1

        if len(top_rev) > 0 and q[1] > top_rev[0]:      # review mới vào mà tốt hơn min trong top review
            out = heapq.heappop(top_rev)
            heapq.heappush(reviews, PQEntry(out))
            heapq.heappush(top_rev, q[1])
        else:
            heapq.heappush(reviews, PQEntry(q[1]))

        if count % 3 == 0:                              # chu kỳ 3 bài thì + 1 bài vô top review
            best_rev = heapq.heappop(reviews).review
            heapq.heappush(top_rev, best_rev)

    # in ra bài tệ nhát trong top review
    if q[0] == 2:
        if len(top_rev):
            print(top_rev[0])
        else:
            print('No reviews yet')


