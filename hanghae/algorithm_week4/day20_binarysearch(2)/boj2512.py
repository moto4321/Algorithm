# 예산 자르기

n = int(input())
lst = list(map(int, input().split()))
m = int(input())

lo = 0
hi = max(lst)

# mid는 상한선!!
while lo <= hi:
    mid = (lo + hi) // 2
    num = 0
    for i in lst:
        if i >= mid:
            num += mid
        else:
            num += i

    if num <= m:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)
