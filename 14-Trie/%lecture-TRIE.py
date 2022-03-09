# 'Trie' lấy từ 'retrieval', hay còn gọi cây từ điển, cây tiền tố
# Trie là cây bth, ko phải cây nhị phân
# Dùng để lưu trữ từ, đối tượng mà khóa tìm kiếm của nó có thể phân tách thành đơn vị

# Độ phức tạp thêm/xóa/tìm kiếm: O(string_length)


# cấu trúc
class Node:
    def __init__(self):
        self.countWord = 0      # nếu số nguyên khác 0 nghĩa là node này là kết thúc 1 từ gồm nhiều chữ cái
        self.child = dict()     # chứa dữ liệu, kết nối vs 1 node khác (C#, Java lưu mảng với số phần tử có sẵn cũng đc, khi xét phải chuyển thành mã ascii
                                #                                      Python dùng dict đơn giản hơn, đỡ phải chuyển thành mã ascii - chr(ord()) rườm rà)


# thêm 1 từ
def addWord(root, s):                   # root ảo nên root là cố định (khác vs BST)
    temp = root
    for ch in s:                        # lấy mã ascii
        if ch not in temp.child:        # chưa có nhánh con
            temp.child[ch] = Node()     # mở rộng nhánh con này
        temp = temp.child[ch]           # temp trượt xuống nhánh con
    # khi hết 1 từ (temp chỉ vào node cuối)
    temp.countWord += 1


# tìm 1 từ
# (gần giống hàm thêm, có 2 TH ko tìm thấy: ko có từ và ko có đủ 1 từ)
def findWord(root, s):
    temp = root
    for ch in s:
        if ch not in temp.child:        # chưa có nhánh con
            return False
        temp = temp.child[ch]           # trượt xuống nhánh con
    return temp.countWord > 0           # rơi vào TH tìm thấy hoặc ko tìm thấy (ko đủ 1 từ)


# xóa 1 từ
# (khi xóa thì:
#   đi xuống cuối cùng giảm count
#   đi lên 1 bước rồi để trả lời 2 câu hỏi:
#       1. count có = 0 chưa (node đó có phải kết thúc 1 từ nào đó hay k)
#       2. có nhánh con ko (node đó có là tiền tố của node nào khác hay k)
# )
# hàm hỗ trợ
# câu hỏi 1: node đó có phải kết thúc 1 từ nào đó hay k
def isWord(node):
    return node.countWord != 0

# câu hỏi 2: sau node đó còn từ nào ko
def isEmpty(node):
    return len(node.child) == 0

# hàm xóa chính (xóa chuỗi s có độ dài len trong cây có root, level: có thể coi độ cao cây, ban đầu = 0)
def removeWord(root, s, level, len):
    if root == None:                    # khi đi xuống tới 1 nhánh rỗng => ko có từ đó
        return False
    if level == len:                    # đã tìm thấy hết tất cả kí tự => thỏa mãn mọi kí tự đều trong cây
        if root.countWord > 0:          # nếu có 1 số từ kết thúc tại root này (cũng là từ s luôn)
            root.countWord -= 1         # giảm 1 đơn vị là đã xóa thành công
            return True
        return False                    # countWord = 0, ko xóa thành công, nghĩa là s ở đây là tiền tố của 1 từ nào đó rồi
    ch = s[level]                       # lấy ra kí tự cần tìm
    if ch not in root.child:            # node con k có
        return False
    flag = removeWord(root.child[ch], s, level + 1, len)                    # đệ quy với level tăng 1, vì đã tìm thấy từ ở level rồi (giống như ở parent nhìn xuống child)
    if flag and not isWord(root.child[ch]) and isEmpty(root.child[ch]):     # xóa thành công k & ko phải kết thúc 1 từ khác & phía dưới ko còn nhánh con
        del root.child[ch]                                                  # quyết định xóa
    return flag


# in toàn bộ từ trong cây, ban đầu cho s =''
def printWord(root, s):
    if isWord(root):            # nếu là 1 từ thì in ra (count > 0)
        print(s)
    for ch in root.child:       # đi xuống nhánh con
        printWord(root.child[ch], s + ch)   # s + ch: + sự chênh lệch của nhánh con vs kí tự hiện tại


if __name__ == '__main__':
    root = Node()
    addWord(root, 'the')
    addWord(root, 'then')
    addWord(root, 'bigo')
    print(findWord(root, 'there'))
    print(findWord(root, 'th'))
    print(findWord(root, 'the'))
    removeWord(root, 'bigo', 0, 4)
    removeWord(root, 'the', 0, 3)
    removeWord(root, 'then', 0, 4)
