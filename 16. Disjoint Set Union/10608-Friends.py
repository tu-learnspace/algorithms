"""
https://onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=1549

- Nếu A và B là bạn bè, B và C cũng là bạn bè => A và C sẽ thành bạn bè
- Cho n người dân và m số cặp người đc cho là bạn của nhau
- Tìm số lượng người trong nhóm bạn bè có nhiều người nhất trong thị trấn

IDEA:
- xem mỗi người là 1 node, quan hệ giữa 2 ng là 1 cạnh
- nếu theo quy tắc bắc cầu A-B-C, ta lại có thêm 1 cạnh nối nữa
=> nối xong sẽ ra đc 1 nhóm người
=> dùng union để nối
- dùng 1 mảng num để chứa thông tin có bao nhiêu đỉnh có đỉnh đó làm đại diện (nghĩa là số bạn chung, vd A-B-C thì mảng num là 2,3,2 -> B là parent có num cao nhất)

- bài này giống bài Prayatna ở lecture 6: DFS => vẫn có thể xài dfs duyệt
"""

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
