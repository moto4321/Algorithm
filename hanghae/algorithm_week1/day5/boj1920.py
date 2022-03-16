# 내 풀이 (시간 초과)

import sys

input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for num in arr2:
    if num in arr1:
        print(1)
    else:
        print(0)


# 이진 탐색 풀이

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(target):
    start = 0
    end = len(arr1) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] == target:
            return True
        elif target < arr1[mid]:
            # start = 0
            end = mid - 1
        elif target > arr1[mid]:
            start = mid + 1
            # end = len(arr1) - 1
    return False


for num in arr2:
    if binary_search(num):
        print(1)
    else:
        print(0)



# 해시테이블 풀이

