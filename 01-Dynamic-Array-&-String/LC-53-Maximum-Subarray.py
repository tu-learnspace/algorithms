"""
https://leetcode.com/problems/maximum-subarray

Cho array, tìm contiguous sub array có sum lớn nhất

IDEA:
Use Kadane algorithm:
- Với mỗi element, tại đó ta đặt câu hỏi max sub là bao nhiêu
- cm đc max sub tại X là X hoặc X + prev max sub)

[ ----- M X --- ]
vd tại X:
- max sub-array chỉ có thể là [X] hoặc [M,X] với M là max sub tại M
- max sub tại element 0 là chính nó

[5, 4, -1, 2]
- max sub tại 5 là [5] -> 5
- max sub tại 4 là [4] hoặc [5][4] -> là [5,4] = 9
- max sub tại -1 là [-1] hoặc [5,4][-1] -> là [5,4,-1] = 8
- max sub tại 2 là [2] hoặc [5,4,-1][2] = 10
-> max sub all là 10

TAKE AWAY:
- remember the pattern
"""


def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_global = max_ending_here = nums[0]

    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], nums[i] + max_ending_here)
        max_global = max(max_global, max_ending_here)

    return max_global


if __name__ == '__main__':
    numArr = [5, 4, -1, 2]
    # numArr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # numArr = [1]
    # numArr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray(numArr)
    print(res)
