from queue import Queue

tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    priors = []
    q = Queue()

    for i in range(n):
        q.put((a[i], i))
        priors.append(a[i])

    priors.sort(reverse=True)

    i = 0
    time = 0
    while not q.empty():
        top = q.get()
        prior = top[0]
        pos = top[1]

        if prior == priors[i]:      # some prior needs to be done first
            time += 1
            i += 1
            if pos == m:
                break
        else:
            q.put((prior, pos))

    print(time)



