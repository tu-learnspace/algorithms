"""
https://lightoj.com/problem/dna-prefix

- có N mẫu DNA là chuỗi các kí tự
- tìm tập con của các mẫu DNA sao cho:
    (chiều dài tiền tố * số lượng ptử tập con có tiền tố đó) là 1 con số lớn nhất
- in ra con số đó

IDEA:
- dùng Trie
- 'số lượng ptử tập con có tiền tố đó' => chính là các nhánh con (node lá) từ level đó
- mỗi node sẽ lưu thêm biến đếm số node lá
=> cứ mỗi khi add 1 char mới và tăng biến đếm lên (nghĩa là khi addWord mới vào mà có đi qua node nào đó thì tăng biến đếm lên)
=> biến đếm tại mỗi node = số lượng nhánh con
- lấy độ dài tại node đó * biến đếm => cập nhật max nếu cần
"""
class Node:
    def __init__(self):
        self.child = dict()
        self.count = 0          # count child

def addWord(root, s):
    global res
    temp = root

    level = 0
    for c in s:
        if c not in temp.child:
            temp.child[c] = Node()

        temp = temp.child[c]
        temp.count += 1         # để đằng sau temp = temp.child[c] mới đúng, vì trượt xuống thì cộng cho con phía dưới (nếu ko thì bị sai ở node cuối)

        level += 1
        res = max(res, temp.count * level)


tc = int(input())
for i in range(tc):
    n = int(input())
    root = Node()
    res = 0
    for _ in range(n):
        s = input()
        addWord(root, s)

    print('Case {}: {}'.format(i + 1, res))
