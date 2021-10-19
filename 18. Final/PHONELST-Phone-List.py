# https://www.spoj.com/problems/PHONELST/

"""

- cho danh sách điện thoại
- kiểm tra có sđt nào là tiền tố của sđt khác ko

IDEA:
- dùng Trie (giống bài Consistency-Checker)
"""

class Node:
    def __init__(self):
        self.child = dict()
        self.countWord = 0


def addWord(root, s):
    temp = root
    for c in s:
        if c not in temp.child:
            temp.child[c] = Node()

        # kiểm tra có từ nào là prefix của s ko
        if temp.child[c].countWord > 0:
            return False

        temp = temp.child[c]  # trượt xuống

    # lúc này temp là node chứa kí tự cuối của s
    temp.countWord += 1

    # kiểm tra phía sau còn node con ko
    if len(temp.child) > 0:
        return False
    return True


tc = int(input())
for _ in range(tc):

    root = Node()
    check = True

    n = int(input())
    for _ in range(n):
        phoneNum = input()
        if check:
            check = addWord(root, phoneNum)

    if check:
        print('YES')
    else:
        print('NO')

