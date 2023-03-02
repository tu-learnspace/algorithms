"""
https://leetcode.com/problems/merge-sorted-array

cho arr1 (m elements) và arr2 (n elements) đã đc sort tăng dần
merge 2 arr lại với nhau và sort tăng dần

note: ko trả ra arr mới, modify trên arr1 -> nên hiển nhiên đề bài sẽ cho arr1 có length = m + n, với n element dư ra = 0
vd:
    nums1 = [1, 2, 3, 0, 0, 0] (nums1 actually [1, 2, 3] thôi nhưng dư ra 3 con 0 để merge vs nums2)
    m = 3
    nums2 = [2, 5, 6]
    n = 3
"""


def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    nums1[m:] = nums2[:n]
    nums1.sort()


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
