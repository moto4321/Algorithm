# 안테나

n = int(input())
home_list = list(map(int, input().split()))

home_list.sort()
# 1, 5, 7, 9

print(home_list[(n - 1) // 2])

