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


# 다른 풀이
n = int(input())
k = int(input())

start, end = 1, k
# k 번째 수는 k보다 클 수 없음

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)

# https://velog.io/@uoayop/BOJ-1300-K%EB%B2%88%EC%A7%B8-%EC%88%98Python