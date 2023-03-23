"""
https://leetcode.com/problems/search-a-2d-matrix/

IDEA:
Với mảng 2d đề cho ta nhận thấy, cứ xét phần tử ở cuối mỗi hàng:
- Phần tử bên trái chắc chắn nhỏ hơn nó
- Phần tử bên dưới chắc chắn lớn hơn nó
=> Áp dụng ý tưởng của binary search
"""


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1  # xét từ phần tử cuối ở hàng

    while row < rows and col > -1:
        curr = matrix[row][col]
        if curr == target:
            return True

        if target > curr:
            row += 1
        else:
            col -= 1

    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    res = searchMatrix(matrix, target)
    print(res)
