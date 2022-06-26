# 나무 자르기
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

start = 0
end = lst[-1]
answer = 0
while start <= end:
    temp = 0
    mid = (start + end) // 2
    for num in lst:
        if num > mid:
            temp += (num - mid)
    if temp >= m:
        answer = max(mid, answer)
        start = mid + 1
    else:
        end = mid - 1


print(answer)