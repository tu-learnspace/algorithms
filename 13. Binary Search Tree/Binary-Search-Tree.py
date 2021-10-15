# BST là cấu trúc dữ liệu dùng để giải quyết các bài toán tìm kiếm mà Binary search ko giải quyết đc
# vì Binary search bth là phải sort trc khi thực hiện => ko hoạt động đc trên dữ liệu linh động

# Các tính chất:
#   Các giá trị trên BST là phân biệt => vì vậy ko handle TH == trong các hàm
#   Mỗi node có nhiều nhất 2 node con
#   Bậc của cây nhị phân là 2 (do mỗi node tối da 2 node con. BSST thì mỗi node chỉ xét bao nhiêu cạnh của node con chứ k phải xét mọi cạnh nối)
#   con trái < node cha, con phải > node cha (giống như mảng đã đc sort trong binary search)


# =====================================================================
# Dùng thư viện (hầu như dùng Red-Black Tree)
# cây nhị phân tự cân bằng: AVL, Red-Black Tree
# C++/Java có thư viện, còn Python ko có => dùng set cài bằng hash table

# DÙNG SET
a = [10, 20, 50, 60, 70]
s = set(a)
# thêm, xóa
s.add(60)
s.remove(60)                        # nếu ko tồn tại thì bị văng error => cần phải kiểm tra trước
if s.remove(30, None) == None:      # => nền xài như này
    print('Object not found')
else:
    print('deleted')
# kiểm tra tồn tại,
if 20 in s:
    print('exists')
# lấy giá trị: set ko có hàm lấy 1 giá trị cụ thể => ta sẽ kiểm tra tồn tại hay ko rồi kết luận
# lấy tất cả phần tử
for value in s:
    print(value)
# thêm ptử set này vào set khác, nếu có key trùng thì bỏ qua
s1.update(s2)
# xóa tất cả phần tử
s.clear()


# DÙNG DICT
d = dict()
# thêm, xóa
d[10] = 'abc'
d[20] = 'def'
d[10] = 'mpk'
val = d.pop(14)                     # nếu ko tồn tại thì bị văng error
if d.pop(30, None) == None:         # nên xài như này
    print('Key not found')
else:
    print('deleted')
# kiểm tra tồn tại
if 20 in d:
    print('exists')
# lấy giá trị theo key
d.get(1)                            # trả về None, nếu xài d[1] là bị văng error
                                    # => khi gán giá trị thì dùng ngoặc vuông, lấy giá trị thì dùng get
# lấy tất cả phần tử
for item in d.items():
    print(item, end=',')
for key in d.keys():
    print(key, end=',')
for value in d.values():
    print(value, end=',')
# thêm ptử set này vào set khác, nếu có key trùng value sẽ đc lấy theo dict thứ 2
d1.update(d2)
# xóa tất cả phần tử
d.clear()


# =====================================================================
# Cài đặt bằng tay
# khai báo cấu trúc 1 node
class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


# tạo 1 node mới
def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode


# insert 1 giá trị mới vào BST
def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x < root.key:
        root.left = insertNode(root.left, x)    # gọi đệ quy sang node con trái, đến khi nào = null nghĩa là đến node lá rồi (vòng if ở trên) thì trả lại node đã tạo. PHép gán sẽ tạo liên kết
    elif x > root.key:
        root.right = insertNode(root.right, x)
    return root


# tạo BST (insert nhiều phần tử vào)
# đối vs heap thì có thể heapify lại từ mảng rất nhanh. Tuy nhiên, BST là danh sách liên kết => phải insert từng phần tử vào
def createTree(a, n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root


# tìm kiếm 1 giá trị trong BST
def searchNode(root, x):
    if root == None or root.key == x:       # ko tìm thấy trả về root, tìm thấy thì cũng trả về root
        return root
    if root.key < x:
        return searchNode(root.right, x)
    return searchNode(root.left, x)


# xóa 1 giá trị trong BST
# tìm node bé nhất trong cây con (hỗ trợ hàm xóa)
def minValueNode(node):
    current = node
    while current.left != None:     # chưa tìm đc thì cứ đi sang trái thôi
        current = current.left
    return current


# hàm chính xóa 1 giá trị trong BST
def deleteNode(root, x):
    if root == None:
        return root
    if x < root.key:                            # TH bé hơn hoặc lớn hơn thì cứ đệ quy tiếp sang trái, phải
        root.left = deleteNode(root.left, x)
    elif x > root.key:
        root.right = deleteNode(root.right, x)
    else:                                       # tìm đc rồi
        if root.left == None:                   # ko có con trái
            temp = root.right                   # đưa con phải lên trên
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        # xuống TH nghĩa là có cả 2 con
        temp = minValueNode(root.right)                 # tìm node nhỏ nhất (trái nhất)
        root.key = temp.key                             # đem node tìm đc lên thành gốc của cây (vì nó có giá trị gần nhất với gốc)
        root.right = deleteNode(root.right, temp.key)   # rồi xóa nó
    return root


# duyệt cây BST (cây bth thì ko có, xài DFS, BFS thôi)
# Inorder Traversal: left -> root -> right => luôn đc mảng tăng dần
# Preorder Traversal: root -> left -> right
# Postorder Traversal: left -> right -> root
# In, pre hay post thật ra chỉ là thứ tự của root
def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        print(root.key, end=' ')
        traversalTree(root.right)


# tính kích thước BST
def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)       # giống thứ tự inorder (post hay pre cũng đc)


# xóa BST
# phải xóa theo thứ tự postorder (vì phải xóa root cuối cùng)
def deleteTree(root):
    if root == None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root

