"""
https://lightoj.com/problem/fibsieves-fantabulous-birthday

"""
import math


tc = int(input())
for i in range(tc):
    time = int(input())

    # calculate table size enough for time
    square = math.ceil(math.sqrt(time))
    r = square * square - time

    x = y = -1
    if r < square:
        y = r + 1
        x = square
    else:
        x = 2 * square - r - 1
        y = square

    if square != 0:
        x, y = y, x

    print('Case {}: {} {}'.format(i + 1, x, y))
