"""
https://www.urionlinejudge.com.br/judge/en/problems/view/1610

- Kiểm tra chuỗi liên kết có chuỗi vòng hay không
- Chuỗi vòng: A liên kết B, B liên kết A (có thể nhiều hơn 2 nút)

- Input:
    + dòng 1: T-số lượng testcase. mỗi tc chứa:
        + dòng đầu: N-số nút M-số mối liên hệ
        + M dòng tiếp theo: A B- cạnh nối A -> B
- Output: in ra YES nếu có chuỗi vòng, ngc lại NO

IDEA:
- duyệt dfs thì sẽ duyệt theo xuôi hết các nhánh
- vì ko chắc chắn các nút đều liên kết với nhau (có ptử ko liên thông) => phải duyệt toàn bộ N đỉnh
- nếu gặp lại node đã visited => có vòng (nên mới quay lại)
"""
MAX = 10**5 + 5

def dfs(src, visited, graph):
    s = []
    visited[src] = True
    s.append(src)

    while len(s) > 0:
        u = s.pop()
        for v in graph[u]:
            if visited[v]:
                return True
            visited[v] = True
            s.append(v)
    return False

if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        graph = [[] for _ in range(MAX)]
        V, E = map(int, input().split())
        for i in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)

        check_loop = False
        for i in range(1, V + 1):
            visited = [False for _ in range(MAX)]
            check_loop = dfs(i, visited, graph)
            if check_loop:
                break

        if check_loop:
            print('YES')
        else:
            print('NO')