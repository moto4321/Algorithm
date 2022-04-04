# 배열의 k번째 큰 요소
# leetcode 215

class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = []
        for elem in nums:
            heapq.heappush(result, (-elem, elem))

        return [heapq.heappop(result) for _ in range(k)][k - 1][1]

