# 떡볶이 떡 만들기

n, m = map(int, input().split())
lst = list(map(int, input().split()))

lst.sort()
lo = 0
hi = max(lst)

while lo <= hi:
    mid = (lo + hi) // 2
    dduk_len = 0
    for dduk in lst:
        if dduk >= mid:
            dduk_len += dduk - mid

    if dduk_len >= m:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)