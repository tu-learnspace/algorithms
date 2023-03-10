def merge_sort(arr):
    # stop condition for recursion: when only 1 left
    if len(arr) <= 1:
        return arr

    """
    split step
    """
    # divide into 2 sub-array
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    # recursion on splitting 2 array
    merge_sort(left_arr)
    merge_sort(right_arr)

    """
    merge step:
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

    # left over last element. TODO: can I use "if" instead of "while"?
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
