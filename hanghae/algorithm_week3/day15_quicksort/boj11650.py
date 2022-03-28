# 좌표 정렬하기

# 내가 푼 풀이
n = int(input())

lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append((x, y))

new_lst = sorted(lst, key=lambda x: (x[0], x[1]))

for a, b in new_lst:
    print(a, b)


