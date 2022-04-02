# 나무 자르기

# 내 풀이
n, m = map(int, (input().split()))
lst = list(map(int, input().split()))

lst.sort() # 10, 15, 17, 20

lo = lst[0]  # 10
hi = lst[-1] # 20
to_go = 0
while lo <= hi:
    temp = 0
    mid = (lo + hi) // 2
    for num in lst:
        if num > mid:
            temp += (num - mid)
    # print(temp)
    if temp >= m:
        to_go = max(mid, to_go)
        lo = mid + 1
    else:
        hi = mid - 1

print(to_go)



# 수정한 풀이 lo를 0부터 시작해줘야합니다...
n, m = map(int, (input().split()))
lst = list(map(int, input().split()))

lst.sort() # 10, 15, 17, 20

lo = 0
hi = lst[-1] # 20
to_go = 0
while lo <= hi:
    temp = 0
    mid = (lo + hi) // 2
    for num in lst:
        if num > mid:
            temp += (num - mid)
    # print(temp)
    if temp >= m:
        to_go = max(mid, to_go)
        lo = mid + 1
    else:
        hi = mid - 1

print(to_go)

