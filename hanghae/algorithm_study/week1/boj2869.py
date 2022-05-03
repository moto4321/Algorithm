a, b, v = map(int, input().split())

day_cnt = (v - b) / (a - b)
print(math.ceil(day_cnt))