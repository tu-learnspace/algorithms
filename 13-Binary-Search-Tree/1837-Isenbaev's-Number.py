"""
https://acm.timus.ru/problem.aspx?space=1&num=1837

- có cuộc thi và các đội thi. nhân vật chính là Isenbaev - là 1 người dự thi
- số Isenbaev như sau:
    con số của chính Isenbaev là 0
    người cùng đội vs Isenbaev là 1
    người chưa cùng đội vs Isenbaev nhưng cùng đội vs người có số 1 sẽ là số 2
    tiếp tục như vậy
- Cho danh sách đội ba người, hãy tính số Isenbaev cho mọi người
- lưu ý: output in ra tên theo thứ tự từ điển: <tên> <số_Isenbaev>

IDEA:
- xem mỗi người là 1 đỉnh trong đồ thị
- có thể thấy trung tâm là Isenbaev, những người chung đội trực tiếp thì đánh số 1, người chung đội vs những người số 1 thì đánh số 2, v.v
=> duyệt BFS từ gốc Isenbaev để biết độ dài của những người khác tới gốc
- quy đổi tên người sang đỉnh đồ thị? => dùng BST để ánh xạ tên thành con số để duyệt BFS. <key,value> = <tên, id>
- có TH Isenbaev ko có trong input => phải check trc khi duyệt bfs vì python sẽ văng lỗi nếu ko có key
- đề yêu cầu in ra thứ tự từ điển => xài python thì phải sort key của dict (vì python là hash)
"""
from queue import Queue
INF = 1e9
MAX = 300                               # tối đa 100 đội, mỗi đội 3 người
id_ = dict()                            # map name to id
nextAvailableID = 0
graph = [[] for _ in range(MAX)]        # danh sách đỉnh kề
dist = [-1 for _ in range(MAX)]         # khoảng cách dist[i] tới gốc (Isenbaev)


def bfs(src):
    q = Queue()
    dist[src] = 0
    q.put(src)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if dist[v] == -1:       # not visited
                dist[v] = dist[u] + 1
                q.put(v)


n = int(input())
for _ in range(n):
    n1, n2, n3 = input().split()    # names
    if n1 not in id_:
        id_[n1] = nextAvailableID
        nextAvailableID += 1
    if n2 not in id_:
        id_[n2] = nextAvailableID
        nextAvailableID += 1
    if n3 not in id_:
        id_[n3] = nextAvailableID
        nextAvailableID += 1

    graph[id_[n1]].extend([id_[n2], id_[n3]])
    graph[id_[n2]].extend([id_[n1], id_[n3]])
    graph[id_[n3]].extend([id_[n1], id_[n2]])

if 'Isenbaev' in id_:        # check vì có thể Isenbaev ko có trong danh sách => python chạy văng keyerror
    bfs(id_['Isenbaev'])

for name in sorted(id_.keys()):
    if dist[id_[name]] != -1:
        print(name, dist[id_[name]])
    else:
        print(name, 'undefined')
