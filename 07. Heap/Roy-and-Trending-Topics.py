"""
https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/

- điểm thịnh hành (hay z-score) của một chủ đề thay đổi mỗi ngày tuân theo quy luật:
    + khi có 1 bài viết liên quan tăng z-score lên 50
    + 1 'Like' tăng z-score lên 5
    + 1 'Comment' tăng z-score lên 10
    + 1 'Share' tăng z-score lên 20
- cần tìm top 5 chủ đề thịnh hành. nếu z-score như nhau thì ưu tiên ID lớn hơn

- input:
    + dòng 1: N-số chủ đề
    + N dòng tiếp theo: <ID> <z-score cũ> <số bài viết> <lượt like> <lượt comment> <lượt share>
- output: xuất ra top 5 thịnh hành, mỗi dòng gồm ID và z-score mới

IDEA:
- sử dụng min heap để lấy ra top 5
- tạo class định nghĩa độ ưu tiên (toán tử >) theo id và độ chênh lệch zscore, lưu thêm zscore mới để in ra
"""
import heapq
h = []

class Topic:
    def __init__(self, id, change, new_score):
        self.id = id
        self.change = change
        self.new_score = new_score

    def __lt__(self, other):
        if self.change == other.change:
            return self.id > other.id
        else:
            return self.change > other.change

n = int(input())
for _ in range(n):
    id, zscore, post, like, cmt, share = list(map(int, input().split()))
    new_score = (post*50 + like*5 + cmt*10 + share*20)
    change = new_score - zscore
    heapq.heappush(h, Topic(id, change, new_score))

for _ in range(5):
    temp = heapq.heappop(h)
    print(temp.id, temp.new_score)