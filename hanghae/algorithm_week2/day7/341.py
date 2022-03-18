# 순열
# leetcode 46

# 내 풀이
class Solution:
    from itertools import permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums, len(nums))


