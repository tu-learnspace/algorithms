"""
https://codeforces.com/problemset/problem/381/A

- Có n lá bài được xếp thành một hàng ngang trên bàn. Trên mỗi lá bài có viết một con số không trùng lặp
- Sereja đi lượt đầu, tiếp theo Dima.
- Trong lượt chơi của mình, người chơi lấy một lá nằm ở bìa trái hoặc phải
- Trò chơi kết thúc khi không còn thẻ bài nào trên bàn nữa
- Người chơi có tổng các số trên lá bài mình đã chọn lớn nhất sẽ chiến thắng
    => Cả 2 đều chọn lá bài có số lớn hơn để lấy trong lượt của mình

- Input:
    + Dòng 1: số nguyên N-số bài trên bàn
    + Dòng 2: chứa N số nguyên-những số đc ghi trên thẻ bài từ trái qua phải
- Output:
    + 1 dòng chứa 2 số nguyên: số điểm của Seraja và Dima khi end game

IDEA:
- Sử dụng 2 con trỏ ở bìa trái & bìa phải. Xem cái nào lớn hơn thì người chơi lượt đó lấy
- Có thể sử dụng thêm biến player_turn đánh dấu lượt chơi của mỗi người kết hợp mảng score
"""
n = int(input())
cards = list(map(int, input().split()))

score = [0, 0]  # lưu trữ score của 2 người
player_turn = 0  # 0: sereja, 1: dima
i = 0
j = n - 1

while i <= j:
    if cards[i] > cards[j]:
        score[player_turn] += cards[i]
        i += 1
    else:
        score[player_turn] += cards[j]
        j -= 1
    player_turn = 1 - player_turn

print(score[0], score[1])

