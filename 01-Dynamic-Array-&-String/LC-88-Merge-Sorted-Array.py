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

    """
    c2 nếu ko xài sort
    vì nums1 nums2 đã đc sort và nums1 chắc chắn là array lớn
    -> dùng 3 con trỏ để lắp vô từ k
    
    [1, 2, 6, 0, 0, 0]
           m        k
    [2, 3, 5]
           n 
    vd: so sánh m vs n là 6 vs 5 (chắc chắn lớn nhất trong mảng) -> có đc 6 chắc chắn lớn nhất -> đem 6 vô k, trừ m
    sau khi so sánh tới 
    
    [3, 3, 3, 0, 0]
    [2, 2]
    TH như này thì phải check sau khi chạy xong mà n vẫn > 0 thì bên n nums2 ráp vô đầu nums1
    """
    # while m > 0 and n > 0:
    #     if nums1[m - 1] > nums2[n - 1]:
    #         nums1[m + n - 1] = nums1[m - 1]
    #         m -= 1
    #     else:
    #         nums1[m + n - 1] = nums2[n - 1]
    #         n -= 1
    # if n > 0:
    #     nums1[:n] = nums2[:n]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    print(nums1)
