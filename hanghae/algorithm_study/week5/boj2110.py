# 공유기 설치
n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()

def binary_search(lst, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = lst[0]
        count = 1

        for i in range(1, n):
            if lst[i] >= current + mid:
                count += 1
                current = lst[i]
        
        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

start = 1
end = lst[-1] - lst[0]
answer = 0

binary_search(lst, start, end)
print(answer)