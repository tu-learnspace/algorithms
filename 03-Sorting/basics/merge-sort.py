"""
MERGE SORT

Time complexity: N LOG N
Divide & conquer:
- divide array in halves
- conquer: repeats itself recursively until all elements become single array elements.
Stable sort (phần tử = nhau giữ nguyên vị trí sau khi sort)
External sort (!= internal sort, input has to be stored in hard drive)
"""
def merge_sort(arr):
    # stop condition for recursion: when only 1 left
    if len(arr) <= 1:
        return arr

    """
    1. split step:
    divide into 2 sub-array
    """
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    # 2. recursion on 2 splited arrays
    merge_sort(left_arr)
    merge_sort(right_arr)

    """
    3. merge step:
    rule: compare <left-most element> vs <left-most element>
    -> use 2 pointers to keep track
    """
    i = 0  # left_arr idx
    j = 0  # right_arr idx
    k = 0  # merge_arr idx
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    """
    4. handle the rest
    """
    # left over last element. TODO: can I use "if" instead of "while"? -> NO
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


if __name__ == '__main__':
    arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    merge_sort(arr_test)
    print(arr_test)
