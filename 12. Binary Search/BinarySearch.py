def binarySearchRecursion(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearchRecursion(a, left, mid - 1, x)
        return binarySearchRecursion(a, mid + 1, right, x)
    return -1


def binarySearch(a, left, right, x):
    while left <= right:    # tại sao ở đây là <=, vì right đc khởi tạo là n-1, vòng while bị phá khi left = right + 1 => nghĩa là [right + 1, right] mới bị phá, còn [right, right] thì vẫn nhận đc chứ k xét thiếu
                            # nói đơn giản search interval là [left, right]
        mid = left + (right - left) // 2  # mid = (left + right) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# tìm phần tử đầu tiên
def binarySearchFist(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:    # tìm đc phần tử và nó phải là phẩn tử đầu tiên (trc nó ko còn ai = x), hoặc đã hết khoảng
            return mid
        elif x > a[mid]:
            return binarySearchFist(a, mid + 1, right, x)
        else:    # trường hợp < và = (nếu = ở đây mà ko rơi vào if trên nghĩa là phía trc vẫn còn ptử = x), nghĩa là quay lên trc tìm
            return binarySearchFist(a, left, mid - 1, x)
    return -1


# tìm phần tử cuối cùng
def binarySearchLast(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == right or x < a[mid + 1]) and a[mid] == x:
            return mid
        elif x < a[mid]:
            return binarySearchLast(a, left, mid - 1, x)
        else:
            return binarySearchLast(a, mid + 1, right, x)
    return -1


# tuy nhiên framework binary search ở trên sẽ ko tìm đc lowerBound vs uppperBound
# tại sao 2 hàm dưới đây ko return -1 như trên? vì phải trả về giá trị chứ k có vụ -1
# vd với lowerBound >=:
# [2, 3, 5, 7] x = 1 thì return 0, [2, 3, 5, 7] x = 8 thì return 4
# có thể hiểu là return số phần tử nhỏ hơn x

# tìm >= đầu tiên
def lowerBound(a, left, right, x):  # tìm x trong mảng a trong khoảng từ left tới right - 1
    pos = right     # ở đây ta chọn right = n, right là phần tử không tìm (vì vậy ở dưới mới là < chứ k phải <=)
                    # nói đơn giản search interval là [left,right)
    while left < right:     # chỉ là < vì thuật toán dừng khi right == left, nghĩa là chạy tới [right -1, right], còn [right,right] thì bị phá (hợp lý vì ta ko muốn lấy right)
        mid = left + (right - left) // 2
        if a[mid] >= x:     # a[mid] là 1 phần tử thỏa đk
            pos = mid       # cập nhật vị trí
            right = mid
        else:               # a[mid] < x  => mid chưa thỏa mãn (lùi lố rồi, tiến lại 1 bước)
            left = mid + 1
    return pos
# tại sao right = mid và left = mid + 1 => vì search interval ở đây là [left, right)
# => mid đc cập nhật phải đc loại bỏ khỏi search interval
# => search interval tiếp theo là [left, mid) hoặc [mid + 1, right)


# tìm > đầu tiên / leftBound
def upperBound(a, left, right, x):  # tìm x trong mảng a trong khoảng từ left tới right - 1
    pos = right     # giả sử ở ngoài mảng => right = n, right là phần tử không tìm (nghĩa là nếu ptử x ko có trong mảng thì ra trả ra right vẫn đúng)
    while left < right:
        mid = left + (right - left) // 2
        if a[mid] > x:     # a[mid] là 1 phần tử thỏa đk (LOWER BOUND CHỈ KHÁC DẤU CHỖ NÀY) => CHỈ CẦN THAY ĐỔI ĐK Ở ĐÂY
            pos = mid       # cập nhật vị trí
            right = mid     # và tìm thằng tốt hơn, ở đây ko right = mid - 1 vì right là cái thằng ko lấy
        else:               # a[mid] < x  => mid chưa thỏa mãn (lùi lố rồi, tiến lại 1 bước)
            left = mid + 1
    return pos

# vậy có thể thay đổi left <= right rồi right = n - 1 được không? vẫn đc, tuy nhiên sẽ có TH left bị out index, ta phải kiểm tra
# vì xét left <= right thì đk dừng là left = right + 1, nếu right = n -1 thì right + 1 = n là out index rồi

# tìm < cuối cùng
def rightBound(a, left, right, x):
    pos = left - 1      # lúc này pos = -1 nghĩa là nếu ptử x ko có trong mảng thì ta trả ra -1 vẫn hợp lý
    while left < right:
        mid = left + (right - left) // 2
        if a[mid] < x:       # thỏa đk nhỏ hơn rồi đó
            pos = mid
            left = mid + 1   # nhưng chắc là tốt nhất chưa?
        else:
            right = mid
    return pos


if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print('{:22s}: {}'.format('search', binarySearch(a, 0, n - 1, x)))    # thường thì hàm này vô nghĩa, ít xài
    print('{:22s}: {}'.format('search fist', binarySearchFist(a, 0, n - 1, x)))
    print('{:22s}: {}'.format('search last', binarySearchLast(a, 0, n - 1, x)))
    print('{:22s}: {}'.format('upper/right bound (>)', upperBound(a, 0, n, x)))  # cái này thực chất là leftBound cũng đc (ptử lớn hơn đầu tiên)
    print('{:22s}: {}'.format('left bound (<)', rightBound(a, 0, n, x)))    # phần tử nhỏ hơn cuối cùng
    print('{:22s}: {}'.format('lower bound (>=)', lowerBound(a, 0, n, x)))   # ptử lớn hơn hoặc bằng đầu tiên

# input
# 15 33
# 6 13 33 33 33 33 51 53 64 72 84 93 95 96 97
# 0 1  2  3  4  5  6  7  8  9  10 11 12 13 14 (index cho dễ theo dõi)
# output:                       thay đổi 33 thành 5:                thay đổi 33 thành 98:
# search            : 3         search                : -1          search                : -1
# search fist       : 2         search fist           : -1          search fist           : -1
# search last       : 5         search last           : -1          search last           : -1
# upper/right bound : 6         upper/right bound (>) : 0           upper/right bound (>) : 15      # lớn hơn đầu tiên
# left bound        : 1         left bound (<)        : -1          left bound (<)        : 14      # bé hơn cuối cùng
# lower bound       : 2         lower bound (>=)      : 0           lower bound (>=)      : 15      # lớn hơn hoặc bằng đầu tiên

# rút ra thêm đc nếu upper bound == lower bonud thì phần tử ko có trong mảng


# đọc để hiểu rõ: https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/detailedbinarysearch

