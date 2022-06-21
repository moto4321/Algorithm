# 공유기 설치
n, c = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort() # [1, 2, 4, 8, 9]

def binary_search(lst, start, end):
    while start <= end:
        mid = (start + end) // 2 # 4
        current = lst[0] # 1
        count = 1

        # mid보다 크거나 같은 때만 설치
        for i in range(1, n): # n = 5
            if lst[i] >= current + mid: 
                count += 1
                current = lst[i]
        
        # 공유기가 목표치 c 만큼 설치가 되었으면
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