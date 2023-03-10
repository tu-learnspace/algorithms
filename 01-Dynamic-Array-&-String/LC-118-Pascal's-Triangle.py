"""
https://leetcode.com/problems/pascals-triangle

C2: you can see the rules below:
1
   1

2
  1 0
  0 1
  1 1 <-

3
 1 1 0
 0 1 1
 1 2 1 <-

4
 1 2 1 0
 0 1 2 1
 1 3 3 1 <-

5
 1 3 3 1 0
 0 1 3 3 1
 1 4 6 4 1 <-

6
 1 4  6  4 1 0
 0 1  4  6 4 1
 1 5 10 10 6 1 <-
"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    """
    C1: native
1        1   
2       1 1
3      1 2 1
4     1 3 3 1
5    1 4 6 4 1

     0 1 2 3 4
    """
    # res = []
    #
    # for i in range(1, numRows + 1):
    #     row = [1] * i
    #     for j in range(1, i - 1):  # bỏ qua 2 phần tử rìa, bỏ đc 2 dòng đầu luôn (at least i = 3 mới vô for đc)
    #         row[j] = res[i - 2][j - 1] + res[i - 2][j]
    #     res.append(row)
    #
    # return res

    """
    C2: explain above
    in Python, [0, 1] + [1, 0] == [0, 1, 1, 0]
    -> need to use lambda: list(map(lambda, value))
    """
    res = [[1]]
    for i in range(1, numRows):
        # [1, 0] + [0, 1] for e.g.
        res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))  # res[-1] means the last element, we want the latest sum
    return res[:numRows]  # TODO: return res? works too


if __name__ == '__main__':
    numRows = 5
    res = generate(numRows)
    print(res)
