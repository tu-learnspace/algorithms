"""
https://leetcode.com/problems/intersection-of-two-arrays-ii

tìm các element có trong nums1 và nums2 (intersect)

IDEA:
c1: sort + 2 pointers
- sort 2 mảng -> đã theo lớn bé thì như đc categorized rồi
- dùng 2 con trỏ kèm 2 mảng để dò intersect

c2: hashmap
giống bài toán đếm số lần lặp lại trong chuỗi
- xài hashmap -> lấy được số lần xuất hiện của phần tử
- có thể tối ưu = việc lấy tập nhỏ hơn làm hash
"""


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    """
    # C1: sort + 2 pointers
    nums1.sort()
    nums2.sort()

    i = j = 0
    res = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            res.append(nums1[i])
            i += 1
            j += 1

    return res
    """
    from collections import Counter

    # C2: hashmap
    # we can optimize space by using smaller array for hashmap
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    # dictionary stores <objects,counts> as <key,value>
    counter = Counter(nums1)
    res = []
    for x in nums2:
        if counter[x] > 0:
            res.append(x)
            counter[x] -= 1  # it's only appear twice (1 from nums1, 1 from nums2)
    return res


if __name__ == '__main__':
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    result = intersect(nums1, nums2)
    print(result)
