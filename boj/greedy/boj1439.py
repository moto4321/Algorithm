# 뒤집기
import math
s = input()
change_cnt = 0

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        change_cnt += 1

print(math.ceil(change_cnt / 2))