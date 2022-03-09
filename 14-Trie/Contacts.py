"""
https://www.hackerrank.com/challenges/contacts/problem

- ứng dụng danh bạ
- có 2 truy vấn:
    add name: lưu name vào danh bạ
    find partial: đếm số lượng liên hệ bắt đầu với partial và in ra số lượng đó
- thực hiện n truy vấn trên

IDEA:
- dùng Trie
- tuy nhiên truy vấn sẽ ko tìm hết 1 từ, mà chỉ tìm tiền tố
=> mỗi node đều lưu countWord để đếm nó là tiền tố của bao nhiêu từ
(tức là nếu có từ mới add vô đi qua nó thì count nó sẽ tăng lên 1 - nó là prefix của từ mới đó)
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
        temp = temp.child[c]
        temp.countWord += 1


def findWord(root, s):
    temp = root

    for c in s:
        if c not in temp.child:
            return 0
        temp = temp.child[c]

    return temp.countWord


root = Node()
q = int(input())
for _ in range(q):
    line = input().split()

    if line[0] == 'add':
        addWord(root, line[1])
    else:
        print(findWord(root, line[1]))

