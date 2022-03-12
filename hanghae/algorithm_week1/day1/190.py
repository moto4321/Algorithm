# 배열 파티션1

# 내 풀이
def arrayPairSum(self, nums: List[int]) -> int:
    nums.sort()
    array = []
    for i in range(0, len(nums), 2):
        item = nums[i:i + 2]
        array.append(item)
    result = 0
    for i in array:
        result += min(i)
    return result


# 답지 1
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum


# 답지 2
def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번쨰 값의 합 계산
        if i % 2 == 0:
            sum += n

    return sum


# 파이썬다운 풀이
def arrayPairSum(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])