# https://leetcode.com/problems/contains-duplicate
"""
Check mảng có chứa phần tử lặp lại không


- Dùng Set (DS k có duplicate element)
"""


def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    return len(nums) != len(set(nums))


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    res = containsDuplicate(nums)
    print(res)
