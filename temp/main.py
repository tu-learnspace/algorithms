def get_sorted_array_original_indexes_1(array):
    """
    use when we want to sort array, but the question wants index of the array before sort

    e.g:
    before sort:
     0  1  2  3  4  5
    [2, 3, 1, 4, 5, 3]

    after sort:
     2  0  1  5  3  4  <- this
    [1, 2, 3, 3, 4, 5]
    """
    sort_index = sorted(range(len(array)), key=lambda k: array[k])  # this means sort the index instead of array
    print(sort_index)


def get_sorted_array_original_indexes_2(array):
    li = []  # array of [value, index]
    for i in range(len(array)):
        li.append([array[i], i])

    li.sort()  # sort [value, index] -> sort base on value
    sort_index = []

    for x in li:
        sort_index.append(x[1])

    print(sort_index)


if __name__ == '__main__':
    arr = [2, 3, 1, 4, 5, 3]
    get_sorted_array_original_indexes_2(arr)
