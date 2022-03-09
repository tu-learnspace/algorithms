"""
https://www.spoj.com/problems/LAZYPROG/

- Cho N công việc. Mỗi công việc có 3 tham số:
    + b: khối lượng công việc (đơn vị thời gian)
    + d: deadline công việc đó
    + a: đơn vị giảm thiểu thời gian nếu trả 1 đô
    => nghĩa là công việc có b thời gian làm thì chỉ còn b - x * a (x là số tiền mình trả)
    => x = b / a nghĩa là trả đủ để hoàn thành công việc liền luôn
- Có thể tùy ý chọn thứ tự làm công việc
- Hãy tìm số tiền ít nhất để mọi công việc đc hoàn thành ĐÚNG deadline

IDEA:
- sắp xếp công việc tăng dần theo deadline (vì công việc nào deadline sớm hớn thì nên hoàn thành trc
=> sort tăng dần theo deadline

- trả thêm cho công việc nào có a lớn nhất để lời hơn
(vd công việc 1 có a lớn hơn công việc 2 => nên thực hiện công việc 1 trc rồi xài tiền thêm ở công việc 1. Vì dẫu công việc 1 đc hoàn thành đúng deadline (ko cần xài tiền) thì mình vẫn nên xài tiền ở công việc 1, đơn giản bởi vì a nó lớn hơn công việc 2 => lời hơn)
=> xài max heap để lấy công việc có a lớn nhất

- tuy nhiên ko đc trả vượt quá khối lg công việc hiện tại (vd a = 10, b = 30 thì trả tối đa 3 đô thôi, ko đc trả 4 đô)
=> phải lưu thêm b vào để check hợp lệ ko (lưu dạng tuple (a, b): khi so sánh ưu tiên a hơn)

- gọi dif là phần chênh lệch giữa khối lượng công việc và deadline. ta muốn giảm dif về = 0 để kịp deadline
- lấy ptử đầu tiên ra khỏi max heap (có a lớn nhất), ptử lấy ra có dạng (a, b).
- Mục tiêu là trả tiền sao cho vẫn hợp lệ - trả tiền ko vượt quá b - b ko bị âm. Có 2 TH:
    + dif > b (chênh lệch lớn quá, b ko đủ => sẽ phải xét thêm ptử tiếp theo để đủ thỏa mãn dif)
        tận dụng hết thời gian còn dư => dif -= b
        xét ptử tiếp theo (vì chưa đủ, dif vẫn dương chứ chưa = 0)
        => số tiền bỏ ra = lượng_xài/a = b/a
    + dif <= b (b lớn hơn dif, b đủ thỏa mãn dif)
        xài ko hết b, lấy xài 1 phần đủ = dif thôi
        chưa xài hết => đẩy vô lại trong max-heap lượng (a, b - dif)
        => số tiền bỏ ra = lượng_xài/a = dif/a

"""
import heapq

tc = int(input())
for _ in range(tc):
    tasks = []

    n = int(input())
    for _ in range(n):
        a, b, d = map(int, input().split())
        tasks.append((d, a, b))

    tasks.sort()        # tự sort ưu tiên d

    pq = []
    currentTime = 0
    money = 0

    for d, a, b in tasks:
        heapq.heappush(pq, (-a, b, d))          # -a vì là max-heap
        currentTime += b

        while currentTime > d:                  # thời gian hoàn thành công việc đó bị lố deadline
            ta, tb, td = heapq.heappop(pq)      # ta mượm thời gian từ công việc có a lớn nhất
            dif = currentTime - d               # chênh lệch giữa thời gian hoàn thành công việc và deadline
            if dif > tb:                        # chênh lệch đó quá lớn, tb ko thỏa mãn nổi
                currentTime -= tb
                money += tb/-ta
            else:                               # dif <= tb, chênh lệch vừa đủ xài
                money += dif/-ta
                heapq.heappush(pq, (ta, tb - dif, d))
                currentTime = d                 # ổn rồi thì break vòng while (hoàn thành đúng deadline)

    print('{:.2f}'.format(money))
