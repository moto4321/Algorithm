n = int(input())
lst = list(map(int, input().split()))
lst.sort()
# -99, -2, -1, 4, 98
INF = 1e9
first = 0
last = len(lst) - 1
prev_val = INF
while True:
    cur_val = lst[first] + lst[last]
    if abs(prev_val) >= abs(cur_val):
        prev_val = cur_val
    # elif 
    if cur_val > 0:
        last -= 1
    elif cur_val < 0:
        first += 1
    else:
        break

