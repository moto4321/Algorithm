# 상위 K 빈도 요소
# leetcode 347
import heapq

freqs = collections.Counter(nums)
freqs_heap = []
# Counter({1: 3, 2: 2, 3: 1})

for f in freqs:
    heapq.heappush(freqs_heap, (-freqs[f], f))

topk = list()

for _ in range(k):
    topk.append(heapq.heappop(freqs_heap)[1])

return topk


# 파이썬 다운 풀이
return list(zip(*collections.Counter(nums).most_common(k)))[0]