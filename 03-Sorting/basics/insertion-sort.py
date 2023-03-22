"""
INSERTION SORT


"""

def insertion_sort(arr):
    for i in range(1, len(arr)):  # bắt đầu tại 1
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
