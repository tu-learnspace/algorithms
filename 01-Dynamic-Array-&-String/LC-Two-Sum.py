"""
https://leetcode.com/problems/two-sum/

Cho mảng, tìm tổng 2 phần tử = target

- use 2 pointers
- sort the input array
- [ 1, 3, 4, 9, 15, 20 ]
- return index, not value -> save original index
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    indexes = sorted(range(len(nums)), key=lambda k: nums[k])

    i = 0
    j = len(nums) - 1

    nums.sort()

    while i < j:
        if nums[i] + nums[j] > target:
            j -= 1
        elif nums[i] + nums[j] < target:
            i += 1
        else:
            return [indexes[i], indexes[j]]

    return [-1, -1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums, target)
    print(res)
