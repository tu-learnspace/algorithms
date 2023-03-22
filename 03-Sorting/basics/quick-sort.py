"""
QUICK SORT

Time complexity: N LOG N
Divide & conquer
Internal sort (input data can be adjusted in memory at once)
Backward: bad when many duplicate elements -> 3-way quicksort (divide into 3: [<] [=] [>])

IDEA:
1. Chọn ra 1 pivot
2. Tạo array từ 3 thành phần: [bên trái nhỏ hơn] pivot [bên phải lớn hơn]
3. Đệ quy tới khi mảng 1 phần tử
4. Ráp lại mảng [trái-pivot-giữa]

Vd với 0 9 3 8 2 7 5, chọn 5 làm pivot, lần lượt từ trái sang phải so sánh vs 5 rồi append left or right
-> 0 3 2  (5)  9 8 7
+ Tiếp tục xét 0 3 2, 2 làm pivot: 0 (2) 3 -> 1 phần tử mỗi bên, dừng
+ Và xét 9 8 7, 7 là pivot: (7) 9 8 -> vẫn còn 2 phần tử, làm tiếp
    + Xét 9 8, 8 làm pivot: (8) 9
-> Như vậy, gộp lại có 0 2 3 (5) 7 8 9
"""

# in-place algorithm
def quick_sort(items):
    if len(items) > 1:
        pivot_index = len(items) // 2
        smaller_items = []
        larger_items = []

        for i, val in enumerate(items):  # i, val in <(0, ele1), (1, ele2), (2, ele3), ...>
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller_items.append(val)
                else:
                    larger_items.append(val)

        # đệ quy để sort cho các sub-array
        quick_sort(smaller_items)
        quick_sort(larger_items)

        """
        pivot đã yên vị ở giữa (sure kèo đúng vị trí), chỉ có 2 sub-array 2 bên chưa sort
        khi đệ quy, items ở đây là của các sub-array thôi -> yên tâm inline
        """
        items[:] = smaller_items + [items[pivot_index]] + larger_items
    # return items

# # not in-place algorithm, but easy to do
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr.pop()
#         larger_items = []
#         smaller_items = []
#
#         for item in arr:
#             if item > pivot:
#                 larger_items.append(item)
#             else:
#                 smaller_items.append(item)
#
#         return quick_sort(smaller_items) + [pivot] + quick_sort(larger_items)


# not really Python-ish code
"""
return pivot index after divide 2 group

e.g.
10 is pivot
  -2 3 -1 5 4 -3 (0)
i j
  -2 3 -1 5 4 -3 (0)
  ij                    # swap to itself
  -2 3 -1 5 4 -3 (0)
   i j                  # nothing happens
  -2 3 -1 5 4 -3 (0)
   i    j               # it's a less 
  -2 -1 3 5 4 -3 (0)
      i j               # -> increase i & swap
  ...
  -2 -1 -3 5 4 3 (0)    # here, move pivot to i + 1
         i     j
"""
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    # phân chia left & right
    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # chuyển pivot ở cuối vào
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1  # pivot index

"""
sort the [l,r] of arr
"""
def quick_sort_2(arr, l, r):
    if l >= r:
        return
    pivot_idx = partition(arr, l, r)  # return the index of pivot after sort (pivot is the last element, after partition it's not the last anymore)

    quick_sort_2(arr, l, pivot_idx - 1)
    quick_sort_2(arr, pivot_idx + 1, r)


if __name__ == '__main__':
    # Python way
    arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    quick_sort(arr_test)
    print(arr_test)

    arr_test_2 = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    quick_sort_2(arr_test_2, 0, len(arr_test_2) - 1)
    print(arr_test_2)
