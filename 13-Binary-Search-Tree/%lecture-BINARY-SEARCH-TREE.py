
# khai báo cấu trúc 1 node: O(1)
class Node:
    def __init__(self):
        self.key = 0
        self.left = None
        self.right = None


# tạo 1 node: O(1)
def createNode(x):
    newNode = Node()
    newNode.key = x
    return newNode


# chèn 1 node vào BST: O(h) với h là chiều cao cây (TH worst là O(n) - cây suy biến)
def insertNode(root, x):
    if root == None:
        return createNode(x)
    if x < root.key:
        root.left = insertNode(root.left, x)
    elif x > root.key:
        root.right = insertNode(root.right, x)
    return root


# tạo BST: O(N * h) với h là chiều cao cây
def createTree(a, n):
    root = None
    for i in range(n):
        root = insertNode(root, a[i])
    return root


# tìm kiếm: O(h) với h là chiều cao cây (worst là O(n))
def searchNode(root, x):
    if root == None or root.key == x:
        return root
    if root.key < x:
        return searchNode(root.right, x)
    return searchNode(root.left, x)


# xóa 1 giá trị trong BST: O(h) với h là chiều cao cây (worst là O(n))
def deleteNode(root, x):
    if root == None:
        return root
    if x < root.key:
        root.left = deleteNode(root.left, x)
    elif x > root.key:
        root.right = deleteNode(root.right, x)
    else:
        if root.left == None:
            temp = root.right
            del root
            return temp
        elif root.right == None:
            temp = root.left
            del root
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root
# hàm hỗ trợ: tìm node nhỏ nhất ở cây con bên phải
def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current


# duyệt cây: O(N)
def traversalTree(root):
    if root != None:
        traversalTree(root.left)
        print(root.key, end=' ')
        traversalTree(root.right)


# tính kích thước cây: O(N)
def size(root):
    if root == None:
        return 0
    return size(root.left) + 1 + size(root.right)


# xóa BST: O(n)
def deleteTree(root):
    if root == None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root


