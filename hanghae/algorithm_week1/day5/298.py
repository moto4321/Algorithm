# 보석과 돌
# leetcode 771

# 해시 테이블을 이용한 풀이
dict = {}

for stone in stones:
    if stone not in dict:
        dict[stone] = 1
    else:
        dict[stone] += 1

count = 0
for jewel in jewels:
    if jewel in dict:
        count += dict[jewel]

return count

# defaultdict를 이용한 풀이
from collections import defaultdict

dict = defaultdict(int)

count = 0
for stone in stones:
    dict[stone] += 1

for jewel in jewels:
    count += dict[jewel]

return count


# Counter를 이용한 풀이
from collections import Counter

dict = Counter(stones)
count = 0

# 비교 없이 보석(jewels) 빈도 수 합산
for jewel in jewels:
    count += dict[jewel]

return count


# 파이썬 다운 풀이
return sum(stone in jewels for stone in stones)