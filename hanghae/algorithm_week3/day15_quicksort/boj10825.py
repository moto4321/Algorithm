# 국영수

n = int(input())

lst = []
for _ in range(n):
    name, k, e, m = input().split()
    lst.append((name, int(k), int(e), int(m)))


new_lst = sorted(lst, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in new_lst:
    print(s[0])