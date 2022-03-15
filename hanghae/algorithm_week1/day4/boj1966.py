# 내 풀이

from collections import deque

x = int(input())

for _ in range(x):
    n, m = map(int, input().split()) # 문서 개수, 궁금한 문서 idx (6, 0)
    prior = deque(list(map(int, input().split()))) # 중요도 [0, 1, 9, 1, 1, 1]
    array = deque([i for i in range(1, n + 1)])         # [1, 2, 3, 4, 5, 6]
    # array = deque([1] * len(n))
    array[m] = 0
    ans = 0
    while True:
        if prior[0] != max(prior):
            prior.append(prior.popleft())
            array.append(array.popleft())
        elif prior[0] == max(prior) and array[0] != 0:
            prior.popleft()
            array.popleft()
            ans += 1
        elif prior[0] == max(prior) and array[0] == 0:
            ans += 1
            print(ans)
            break