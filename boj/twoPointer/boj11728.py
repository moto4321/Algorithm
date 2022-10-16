n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_list = a + b

new_list.sort()

for i in new_list:
    print(i, end=" ")