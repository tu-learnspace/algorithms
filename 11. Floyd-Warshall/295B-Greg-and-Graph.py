"""
https://codeforces.com/problemset/problem/295/B

- trong đồ thị này bất kì các cặp đỉnh phân biệt nào cũng có cạnh hai chiều ở giữa chúng
- mỗi bước sẽ xóa lần lượt từng đỉnh
- tính tổng độ đài của tất cả các đường đi ngắn nhất giữa tất cả các cặp đỉnh trước khi bắt đầu xóa đỉnh

IDEA:
- thay vì mỗi bước xóa 1 đỉnh như thứ tự bth => rất phức tạp
=> làm ngc lại, bắt đầu từ bước cuối cùng đi ngc lại bc đầu tiên
=> giống như lần lượt thêm từng nút vào đồ thị (đến bc đầu tiên là đồ thị hoàn chỉnh nhất). Nghĩa là mỗi bước thêm một đỉnh mới vào giống như thêm 1 đỉnh trung gian K vào, chạy floyd xem nó có tốt hơn ko thì cập nhật dist
- in kq theo hướng ngc lại => như v phải lưu kq vào 1 mảng
- vì khi đi ngc lại là chắc chắn có đường => ko cần check INF
"""

n = int(input())
dist = [[0] * (n + 1)]  # bắt đầu từ 1

for i in range(1, n + 1):
    dist.append([0] + list(map(int, input().split())))

middleV = list(map(int, input().split()))       # danh sách các đỉnh lần lượt bị xóa. ta xem như đây là 1 đỉnh trung gian K
res = [0] * n

for index in range(n - 1, -1, -1):              # duyệt ngc từ cuối về đầu
    k = middleV[index]

    # floyd-warshall
    # xét mỗi cặp đỉnh i, j thì chèn k vào có tốt hơn ko
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:        # ko cần check INF
                dist[i][j] = dist[i][k] + dist[k][j]

    # cập nhật kết quả từ đỉnh cuối về đỉnh đầu
    for u in middleV[index:]:
        for v in middleV[index:]:
            res[index] += dist[u][v]

print(*res)


