"""
https://leetcode.com/problems/valid-sudoku

Cho sudoku 9x9, kiểm tra nếu sudoku valid:
- hàng phải chứa 1->9
- cột phải chứa 1->9
- trong ô 3x3 phải chứa 1->9

IDEA:
các criteria đều check phần tử ko lặp lại
-> sài set, tạo arr 3 phần tử là 3 set tương ứng vs các criteria
"""


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    check = []
    for i in range(9):
        for j in range(9):
            element = board[i][j]
            if element != ".":  # mỗi tuple phải khác nhau format để không bị lẫn
                check += [(i, element), (element, j), (i // 3, j // 3, element)] # dùng check.extend cũng được

    return len(check) == len(set(check))


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    res = isValidSudoku(board)
    print(res)
