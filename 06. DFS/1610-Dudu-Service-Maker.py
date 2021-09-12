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
- bài toán tìm đường, tìm vòng => xài dfs duyệt sâu là hợp lý nhất
- nếu gặp lại node đã visited => có vòng
- sẽ có trường hợp node bắt đầu ko kề vs một số node khác => phải duyệt toàn bộ N đỉnh
- sau khi đã duyệt từ đỉnh nào đó mà ko thấy vòng => nên check điểm đó lại để khỏi duyệt phần đó nữa (mất công TLE)
=> mảng visited để đánh dấu thăm node đó chưa. tuy nhiên ko chỉ true false mà mang giá trị 0 1 2
    + 0: chưa visited
    + 1: đã visited => xài khi dfs thì 1 điểm bắt đầu. nếu gặp 1 => có vòng
    + 2: đã dfs từ đỉnh này rồi => ko cần xét đỉnh này (khi duyệt dfs đỉnh khác mà gặp đỉnh 2 thỉ bỏ qua)

- Useful testcase:
1
6 6
1 6
2 5
3 1
3 5
4 2
5 4
=> output: YES
"""
import sys
sys.setrecursionlimit(10 ** 6)
MAX = 10**5 + 5

def dfs(src, visited, graph):
    visited[src] = 1
    for v in graph[src]:
        if visited[v] == 1:    # khẳng định có vòng return luôn (trong đây ta ko check visited = 2-những con đường đã duyệt mà ko có vòng)
            return True
        elif visited[v] == 0:
            res = dfs(v, visited, graph)
            if res:             # ở đâu cũng phải return luôn để ko xuống dưới kia mark = 2
                return True
    visited[src] = 2    # đi hết đường từ src rồi mà ko tìm ra vòng => mark lại = 2 để lần duyệt sau ko vào con đường này nữa
    return False


if __name__ == '__main__':
    testcase = int(input())
    for _ in range(testcase):
        graph = [[] for _ in range(MAX)]
        V, E = map(int, input().split())
        for i in range(E):
            u, v = map(int, input().split())
            graph[u].append(v)
        visited = [0] * (V + 1)

        check = False
        for i in range(1, V + 1):
            if visited[i] == 0:
                check = dfs(i, visited, graph)
                if check:
                    break

        if check:
            print('YES')
        else:
            print('NO')