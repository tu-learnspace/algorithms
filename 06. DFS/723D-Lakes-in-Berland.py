"""
https://codeforces.com/problemset/problem/723/D?locale=en

- '.' biểu thị ô nước, '*' là ô đất
- cho mảnh đất berland. cần tìm số ô nước ít nhất cần lấp lại sao cho thỏa số hồ còn lại
- chỉ lấp hồ (là những ô nước đc bao bọc trong đất liền)

- Input:
    + dòng 1: n,m-kích thước mảnh đất k-số hồ mong muốn còn lại sau khi lấp
    + n dòng tiếp theo: hiển thị mảnh đất
- Output:
    + dòng 1: in số ô ít nhất càn lấp
    + n dòng tiếp theo: hiển thị mảnh đất sau khi lấp hồ

IDEA:
- duyệt cả vùng đất ngoại trừ # và 4 cạnh rìa
- đếm tổng số hồ - số hồ mong muốn bị lấp => số hồ phải lấp
- 
"""


if __name__ == '__main__':
    n, m, k = map(int, input().split())

