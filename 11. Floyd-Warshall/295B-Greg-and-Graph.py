"""
https://codeforces.com/problemset/problem/295/B

- trong đồ thị này bất kì các cặp đỉnh phân biệt nào cũng có cạnh hai chiều ở giữa chúng
- mỗi bước sẽ xóa lần lượt từng đỉnh
- tính tổng độ đài của tất cả các đường đi ngắn nhất giữa tất cả các cặp đỉnh trước khi bắt đầu xóa đỉnh

IDEA:
- thay vì mỗi bước xóa 1 đỉnh như thứ tự bth => rất phức tạp
=> làm ngc lại, bắt đầu từ bước cuối cùng đi ngc lại bc đầu tiên => giống như lần lượt thêm từng nút vào đồ thị (đến bc đầu tiên là đồ thị hoàn chỉnh nhất)
- với mỗi bước đi ngc lại thì dùng floyd để tính đường đi ngắn nhất giữa tất cả cặp đỉnh
- in kq theo hướng ngc lại => như v phải lưu kq vào 1 mảng
- vì khi đi ngc lại là chắc chắn có đường => ko cần check INF
"""

def backward_floyd():
    for k in range(n - 1, -1, -1):
        for i in range(n):
            for j in range(n):
                if graph[i][j] < graph[i][deleted[k]] + graph[deleted[k]][j]:
                    graph[i][j] = graph[i][deleted[k]] + graph[deleted[k]][j]

    for i in range(n):
        for j in range(n):
            ans += graph[][]


n = int(input())
graph = [0] * (n + 1)
for i in range(n):
    graph[i] = list(map(int, input().split()))

deleted = list(map(int, input().split()))

res = [0] * (n + 1)

backward_floyd()

