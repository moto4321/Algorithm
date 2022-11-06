n, k = map(int, input().split()) # 9, 2
lst = list(map(int, input().split())) # 3 2 5 5 6 4 4 5 7
left, right = 0, 0

counter = [0] * (max(lst) + 1)
answer = 0
while right < n:
    if counter[lst[right]] < k: # counter[lst[0] == 3] < 2
        counter[lst[right]] += 1
        right += 1
    else:
        counter[lst[left]] -= 1
        left += 1
    answer = max(answer, right - left)

print(answer)
