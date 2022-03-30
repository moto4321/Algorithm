# 수 정렬하기2

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

for num in sorted(lst):
    print(num)