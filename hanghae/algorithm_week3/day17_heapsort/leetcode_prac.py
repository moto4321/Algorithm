# leetcode 973

# 내 풀이 실패
import heapq

def k_closest_builtin(points, k):
    dists = []
    heap = []
    for point in points:
        dist = point[0]**2 + point[1]**2
        heapq.heappush(heap, dist)
        dists.append(dist)

    kth_dist = [heapq.heappop(heap) for _ in range(k)][-1]
    return [points[idx] for idx, dist in enumerate(dists) if dist <= kth_dist]




class Solution:
    import heapq

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_list = []

        for x, y in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(dist_list, dist)

        ordered_dist = [heapq.heappop(dist_list) for _ in range(k)][-1]

        # print(ordered_dist)
        # dist_list = [8, 10]
        # points = [[1, 3], [-2, 2]]
        # ordered_dist = [8]

        return [points[idx] for idx, dist in enumerate(dist_list) if dist <= ordered_dist]
