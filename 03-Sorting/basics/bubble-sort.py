"""
BUBBLE SORT

Mỗi lần lặp, ptử min sẽ được đưa lên


IDEA:

"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    bubble_sort(arr_test)
    print(arr_test)
