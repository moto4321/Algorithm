# 랜선 자르기

k, n = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))

lst.sort()

lo = 1
hi = max(lst)
while lo <= hi:
    mid = (lo + hi) // 2
    lan_cnt = 0
    for lan in lst:
        lan_cnt += lan // mid

    if lan_cnt >= n:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)