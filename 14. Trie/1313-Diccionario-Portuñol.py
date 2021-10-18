"""
https://www.urionlinejudge.com.br/judge/en/problems/view/1313

- cho danh sách gồm:
    P từ tiếng Portugal
    S từ tiếng Spanish
- một từ mới đc tạo bởi công thức: pre + suf
    pre: tiền tố KHÔNG RỖNG của 1 từ trong danh sách tiếng Portugal
    suf: hậu tố KHÔNG RỖNG của 1 từ trong danh sách tiếng Spanish
- hãy tìm số từ có thể tạo đc bởi quy luật trên

IDEA:
- đếm số tiền tố & hậu tố của tất cả các từ rồi * lại (như toán tổ hợp)
- tuy nhiên sẽ bị trùng => đếm số tiền tố & hậu tố khác nhau
=> dùng 2 cây Trie, 1 cây lưu tiền tố tiếng P, 1 cây lưu hậu tố tiếng S
- Cây Trie 1 có X nút, cây Trie 2 có Y nút => số cách chọn là X * Y => nhưng vẫn sai do các cách ghép pre-suff
=> phải duyệt DFS rồi đêm

- tóm lại, có 2 TH bị trùng:
    + trùng do các prefix trùng nhau, các suffix trùng nhau
        => dùng cây Trie lưu trữ các từ (lưu ý tiếng S lưu dảo ngược vì là hậu tố)
        => đếm đc kích thước 2 cây là X, Y
    + trùng do ghép các prefix và suffix
        => đếm số lần xuất hiện của chữ cái trong cây (trừ các node nối liền vs root)
        => hàm f(x) và g(X) (với x là các chữ cái)
        => lấy Z = tổng f(x)*g(X)
    => KQ = X * Y - Z

"""
import string
import sys
sys.setrecursionlimit(10000000)

class Node:
    def __init__(self):
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = Node()
        self.size = 0

    def addWord(self, word):
        temp = self.root
        for c in word:
            if c not in temp.child:
                temp.child = Node()
                self.size += 1
            temp = temp.child

# đếm số nút
def dfs(root, count, isRoot):
    # alphabet = {c: 0 for c in string.ascii_lowercase}
    alphabet = list(string.ascii_lowercase)          # mảng các chữ cái

    for c in alphabet:
        if root.root.child[c]:
            count[c] += not isRoot
            dfs(root.root.child[c], count, 0)



while True:
    p, s = map(int, input().split())
    if p == 0 and s == 0:
        break

    suffix_trie = Trie()
    prefix_trie = Trie()

    for _ in range(p):
        s = input()
        prefix_trie.addWord(s)

    for _ in range(s):
        s = input()
        suffix_trie.addWord(s[::-1])        # reverser

    ans = suffix_trie.size * prefix_trie.size

    f = [0] * 26
    g = [0] * 26

    dfs(suffix_trie, f, 1)
    dfs(prefix_trie, g, 1)

    for i in range(26):
        ans -= f[i] * g[i]
