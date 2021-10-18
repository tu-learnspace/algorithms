"""
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/description/

- giống chức năng auto-complete
- cho 1 tập dữ liệu nhiều xâu, mỗi xâu có 1 độ ưu tiên đại diện
- với mỗi từ khóa tìm kiếm (truy vấn), in ra độ ưu tiên lớn nhất của xâu nhận từ khóa tìm kiếm là tiền tố

IDEA:
- search theo từ => dùng Trie
- thay vì lưu countWord = 1 thì lưu độ ưu tiên ở node cuối cùng của xâu
=> phải duyệt đến node cuối cùng của xâu để lấy độ ưu tiên
=> ĐPT O(n*str_len - để addWord + q*str_len*n - truy vấn) => có thể bị TLE
=> thay vì lưu độ ưu tiên ở node cuối cùng => lưu thêm độ ưu tiên lớn nhất của node tại mỗi node
=> với mỗi truy vấn, vd 'hacker', ta chỉ cần duyệt các node 'h','a','c','k','e','r' rồi lấy ra độ ưu tiên cao nhất trong chúng
"""


class Node:
    def __init__(self):
        self.child = dict()
        self.maxPrior = -1


def addWord(root, str, priority):
    temp = root
    for ch in str:
        if ch not in temp.child:
            temp.child[ch] = Node()

        temp.maxPrior = max(temp.maxPrior, priority)

        temp = temp.child[ch]                           # trượt xuống


def getMaxPrior(root, str):
    temp = root
    for ch in str:
        if ch not in temp.child:
            return -1
        temp = temp.child[ch]
    return temp.maxPrior


root = Node()
n, q = map(int, input().split())
for _ in range(n):
    string, prior = input().split()
    addWord(root, string, int(prior))

for _ in range(q):
    query = input()
    print(getMaxPrior(root, query))




