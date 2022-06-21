# K번째 수
n = int(input())
k = int(input())

# lst = [[(i + 1) for i in range(n)] for j in range(n)]
lst = []
for i in range(n):
    for j in range(n):
        lst.append((i + 1) * (j + 1))

lst.sort()

print(lst[k])

# 메모리 제한때문에 틀림

# 정답
n = int(input())
k = int(input())

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n + 1):
            cnt += min(mid // i, n)
        
        if cnt >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

print(binary_search(k, 1, n * n))