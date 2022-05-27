# 스택
import sys
input = sys.stdin.readline
stack = []
def push(n):
    stack.append(n)

def pop(stack):
    if len(stack) != 0:
        print(stack.pop())
    else:
        print(-1)


def size(stack):
    print(len(stack))

def empty(stack):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top(stack):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

num = int(input())
for _ in range(num):
    order = list(input().split())
    if order[0] == 'push':
        push(int(order[1]))
    elif order[0] == 'pop':
        pop(stack)
    elif order[0] == 'size':
        size(stack)
    elif order[0] == 'empty':
        empty(stack)
    elif order[0] == 'top':
        top(stack)
