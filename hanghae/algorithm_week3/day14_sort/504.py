# 가장 큰 수
# leetcode 179

# 처음에 푼 풀이(틀림)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        reset = []
        for num in nums:
            reset.append(str(num))

        reset.sort(key=lambda x: x[0], reverse=True)

        return ''.join(reset)


# 답
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        iters = len(nums) - 1
        for iter in range(iters):
            wall = iters - iter
            for cur in range(wall):
                if str(nums[cur]) + str(nums[cur + 1]) < str(nums[cur + 1]) + str(nums[cur]):
                    nums[cur], nums[cur + 1] = nums[cur + 1], nums[cur]

        return str(int(''.join(map(str, nums))))