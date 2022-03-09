"""
https://lightoj.com/problem/consistency-checker

- cho dữ liệu là các chuỗi tín hiệu
- nếu trong bộ dữ liệu có 1 chuỗi tín hiệu là tiền tố của chuỗi tín hiệu khác => inconsistent
- ngc lại => consistent
- xác định loại bộ dữ liệu đó là inconsistent (in NO) hay consistent (in YES)

IDEA:
- xác định nếu có 1 chuỗi là tiền tố của chuỗi khác ko
=> xây dựng cây Trie
- kiểm tra dữ liệu khi thêm vào cây Trie:
    có chứa chuỗi khác làm tiền tố ko
        => khi addWord vào mà gặp countWord = 1 => đã có 1 từ nào đó làm tiền tố rồi
    có là tiền tố của chuỗi khác ko
        => nghĩa là addWord xong rồi mà đằng sau vẫn còn node => chuỗi mới add vào là tiền tố của 1 chuỗi nào đó
        => kiểm tra node chứa ký tự cuối có node con k
- vừa check 2đk trên lúc thêm vào => kết luận đc luôn
"""

class Node:
    def __init__(self):
        self.child = dict()     # chứa tối đa 10
        self.countWord = 0

# trả về False nếu s thêm vào là tiền tố của chuỗi khác
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
for i in range(tc):
    root = Node()
    consistent = True

    n = int(input())
    for _ in range(n):
        s = input()
        if consistent:
            consistent = addWord(root, s)

    if consistent:
        print('Case {}: {}'.format(i + 1, 'YES'))
    else:
        print('Case {}: {}'.format(i + 1, 'NO'))

