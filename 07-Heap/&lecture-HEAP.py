# với mỗi vị trí từ n/2 - 1 (node cha cuối cùng có con), gọi hàm heapify để xem nhánh con có vi phạm ko
# (trong hàm heapify lại kiểm tra và gọi đệ quy xuống phía dưới để ktra vi phạm)

# chuẩn hóa cây con có nút gốc là i
def minHeapify(i):
    smallest = i        # tạm thời cho cha là nhỏ nhất để xét coi có vi phạm ko
    left = 2*i + 1      # tính vị trí con trái
    right = 2*i + 2     # tính vị trí con phải

    # nếu maxheap thì chỉ cần đảo dấu < thành > ở 2 vòng if dưới thôi
    # vì các lần đệ quy xuống có thể đệ quy lố cái cuối nên phải check index con trái có tồn tại ko (< len(h))
    if left < len(h) and h[left] < h[smallest]:     # nếu con trái tồn tại & con trái nhỏ nhất
        smallest = left
    if right < len(h) and h[right] < h[smallest]:   # ________ phải _______& con phải nhỏ nhất
        smallest = right

    # sau khi 2 if trên thì smallest là giá trị nhỏ nhất trong 3 cha con
    if smallest != i:                               # nếu nhỏ nhất ko phải là cha => có sự vi phạm
        h[i], h[smallest] = h[smallest], h[i]       # đảo cha con
        minHeapify(smallest)                        # phía dưới có thể vi phạm nên đệ quy xuống phía dưới


# thực hiện chuẩn hóa cây từ vị trí cuối cùng có node lá
def buildHeap(n):
    for i in range(n//2 - 1, -1, -1):   # duyệt từ node index n/2 - 1 về trước (vì đó là node cha cuối cùng có con)
        minHeapify(i)                   # với mỗi node cha như vậy thì gọi heapify


# thêm phần tử vào heap
def push(value):
    h.append(value)     # thêm vào cuối
    i = len(h) - 1
    # con = cha * 2 + 1 => cha = (con - 1) / 2
    while i != 0 and h[(i-1) // 2] > h[i]:              # nếu cha > con => vi phạm; đk i != 0 để nhảy từ dưới lên xem có vi phạm ko thì đảo
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]   # đổi chỗ cha con
        i = (i - 1) // 2                                # nhảy i lên vị trí node cha mới để xem có sai ko, sai thì tiếp túc đảo đến khi i = 0 là đỉnh thì break while


# xóa phần tử khởi heap
def pop():
    length = len(h)
    if length == 0:             # heap đang rỗng
        return
    h[0] = h[length - 1]        # swap cuối & đầu
    h.pop()
    minHeapify(0)               # chuẩn hóa lại từ đầu


if __name__ == '__main__':
    h = [7, 12, 6, 10, 17, 15, 2, 4]
    buildHeap(len(h))
    print(h)