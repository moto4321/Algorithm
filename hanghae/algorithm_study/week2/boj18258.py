import sys
from collections import deque
input = sys.stdin.readline
q = deque([])
def push(q, x):
    q.append(x)

def pop(q):
    if len(q) != 0:
        print(q.popleft())
    else:
        print(-1)

def size(q):
    print(len(q))

def empty(q):
    if len(q) == 0:
        print(1)
    else:
        print(0)

def front(q):
    if len(q) != 0:
        print(q[0])
    else:
        print(-1)

def back(q):
    if len(q) != 0:
        print(q[-1])
    else:
        print(-1)

t = int(input())
for _ in range(t):
    order = input().split()
    if order[0] == 'push':
        push(q, order[1])
    elif order[0] == 'pop':
        pop(q)
    elif order[0] == 'size':
        size(q)
    elif order[0] == 'empty':
        empty(q)
    elif order[0] == 'front':
        front(q)
    elif order[0] == 'back':
        back(q)