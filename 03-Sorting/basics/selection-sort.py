"""
SELECTION SORT

Loop 2 vòng. 1 vòng là mỗi ptử, với mỗi ptử, ta phải sure đó là ptử min
(tức là loop vòng 2 cho tất cả ptử còn lại, if có đứa min hơn thì swap)

IDEA:
Với mỗi phần tử:
- xem như ptử đó là min
- lặp tới tất cả phần tử còn lại để ráng tìm 1 ptử min khác nhỏ hơn
- swap 2 phần tử đó
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    selection_sort(arr_test)
    print(arr_test)
