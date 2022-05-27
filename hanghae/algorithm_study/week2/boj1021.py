# 회전하는 큐
from collections import deque
n, m = map(int, input().split())
num = list(map(int, input().split()))

q = deque([(i + 1) for i in range(n)])

def left(q):
    q.append(q.popleft())

def right(q):
    q.appendleft(q.pop())

count = 0
for i in num:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q) / 2:
                while q[0] != i:
                    left(q)
                    count += 1
            else:
                while q[0] != i:
                    right(q)
                    count += 1

print(count)