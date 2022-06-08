n = int(input())
lst = list(map(int, input().split()))

new_lst = sorted(lst) # [1, 2, 3, 3, 4]

answer = 0
for i in range(len(new_lst)):
    each_time = 0
    for j in range(i + 1):
        each_time += new_lst[j]
    answer += each_time

print(answer)