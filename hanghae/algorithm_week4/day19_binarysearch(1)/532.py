# leetcode 167

# 포인터를 하나씩 좁혀가면서 풀이
left, right = 0, len(numbers) - 1
while not left == right:
    if numbers[left] + numbers[right] < target:
        left += 1
    elif numbers[left] + numbers[right] > target:
        right -= 1
    else:
        return [left + 1, right + 1]

# 이진탐색을 이용한 풀이...
for idx, num in enumerate(numbers):
    left, right = idx + 1, len(numbers) - 1
    expected = target - num
    # 이진 검색으로 나머지 값 판별
    while left <= right:
        mid = left + (right - left) // 2
        if numbers[mid] < expected:
            left = mid + 1
        elif numbers[mid] > expected:
            right = mid - 1
        else:
            return idx + 1, mid + 1

