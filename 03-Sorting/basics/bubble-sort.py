"""
BUBBLE SORT

Lần lượt từ trái qua phải, so sánh từng CẶP rồi swap
-> ptử min sẽ được đưa lên đầu (cuối mảng)
Tiếp tục lặp lại


"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):  # giảm đi 1 (trừ đi các phần tử đã được bubbling lên đầu)
            if arr[j] > arr[j + 1]:  # vì ta so sánh từng cặp nên ko xài i ở đây
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr_test = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    bubble_sort(arr_test)
    print(arr_test)
