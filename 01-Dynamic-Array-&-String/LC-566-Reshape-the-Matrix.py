"""
https://leetcode.com/problems/reshape-the-matrix

2x2
1 2
3 4

1x4
1 2 3 4

4x1
1
2
3
4
-> feasible if the plus equal

  0 1 2
0 1 2 3
1 4 5 6

  0 1
0 1 2   k
1 3 4
2 5 6

TAKEAWAY:
Formula for transform 1D -> 2D array:
   k from 0 -> cols
   output[k // c][k % c] = arr[i][j]

To remember:
- output [rol][col] = arr[i][j] <- loop through all element [i, j]. i, j iterate through existing_col & existing_row
- Above example, we see that number of columns will decide the number of truncate -> chỉ cần quan tâm số cột, số dòng tự sinh ra dựa vào việc cắt theo cột
->  rol = k // expected_col (cắt bao nhiu đoạn nhỏ là do số cột quyết định -> dùng phép chia nguyên để tìm số cột)
    col = k % expected_col (dư ra bao nhiêu nó tự tràn xuống -> tự quyết định số dòng = phép module)

"""

def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    rows = len(mat)
    cols = len(mat[0])
    if rows*cols != r*c:
        return mat
    res = [[0 for _ in range(c)] for _ in range(r)]

    # C1: 1 loop, run time the same but save memory (k variable)
    # for i in range(rows*cols):
    #     res[i // c][i % c] = mat[i // cols][i % cols]

    # C2: 2 loops
    k = 0
    for i in range(rows):
        for j in range(cols):
            res[k // c][k % c] = mat[i][j]
            k += 1

    return res


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6]]
    r = 3
    c = 2
    res = matrixReshape(mat, r, c)
    print(res)
