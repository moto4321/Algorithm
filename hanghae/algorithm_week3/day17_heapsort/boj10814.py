# 나이순 정렬

n = int(input())

lst = []
for i in range(n):
    age, name = input().split()
    lst.append((int(age), name, i))

lst.sort(key=lambda x: (x[0], x[2]))

for li in lst:
    print(li[0], li[1])



# 힙정렬을 이용한 풀이
import heapq

n = int(input())
queue = []
list = []

for i in range(n):
  age, name = input().split()
  heapq.heappush(queue,(int(age), i, name))

for i in range(n):
  list.append(heapq.heappop(queue))
  print(list[i][0], list[i][2])