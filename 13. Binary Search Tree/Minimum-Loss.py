"""
https://www.hackerrank.com/challenges/minimum-loss/problem

- có giá nhà năm thứ i là pi trong n năm
- mua & bán lại nhà sao cho giảm thiểu thua lỗ theo quy tắc:
    ko thể bán đi vs giá lớn hơn hoặc bằng lúc đc mua (lúc bán sẽ chịu lỗ)
    ko thể bán đi trong cùng năm nó đc mua vào
- tìm lượng tiền nhỏ nhất sẽ mất khi mua và bán nhà trong n năm tiếp theo

IDEA:
- cho 1 mảng các phần tử, tìm hiệu 2 phẩn tử sao cho hiệu nhỏ nhất

C1: làm bth
- sort mảng tăng dần
- lần lượt lấy hiệu 2 phần tử kề nhau để tìm minimum loss
- chú ý check index 2 phần tử trong mảng gốc phải hợp lý (thỏa việc mua rồi mới bán)
- vì đề bài cho 1 < p < 10^16 nên cho INF lớn hơn

C2: xài BST
=> tìm giá tiền nhỏ hơn giá ở năm thứ i nhưng lại nhỏ nhất trong các giá từ năm 1 đến năm i-1 (lớn nhất trong các cái bé nhất)
- duyệt từng ptử i, lấy ra ptử lớn hơn nó nhưng nhỏ nhất rồi xem hiệu 2 ptử đó có là min k
=> bỏ ptử 1 đến ptử thứ i-1 vào BST để tìm upper bound
"""
# Cách 1
INF = 1e17


def minimunloss(prices):
    sortPrices = sorted(prices)
    minloss = INF

    for i in range(n - 1):
        loss = sortPrices[i + 1] - sortPrices[i]
        if loss < minloss and (prices.index(sortPrices[i]) > prices.index(sortPrices[i + 1])):  # phải mua rồi mới bán
            minloss = loss

    return minloss


n = int(input())
prices = list(map(int, input().split()))

print(minimunloss(prices))

# Cách 2:
# implement BST trong python
# class Node:
#    def __init__(self, value):
#       self.value = value
#       self.left = self.right = None
#
# def insert(root, x):
#    if root is None:
#       return Node(x)
#    if x < root.value:
#       root.left = insert(root.left, x)
#    elif x > root.value:
#       root.right = insert(root.right, x)
#    return root
#
# # tìm cận trên > x
# def upperbound(root, x):
#    if root is None:
#       return root
#    if root.value <= x:
#       return upperbound(root.right, x)
#    elif root.value > x:
#       ub_left = upperbound(root.left, x)
#       if ub_left is None:
#           return root
#       else:
#           return ub_left
#
#
# n = input()
# prices = list(map(int, input().split()))
#
# minimum_loss = 10 ** 16
# root = None
#
# for sell_price in prices:
#    best_buy_node = upperbound(root, sell_price)     # tìm upperbound (>) của mỗi ptử
#    if best_buy_node is not None:                    # nếu tìm đc
#       minimum_loss = min(best_buy_node.value - sell_price, minimum_loss)    # cập nhật min nếu cần
#    root = insert(root, sell_price)
#
# print(minimum_loss)
