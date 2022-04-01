# leetcode 240

# 내가 처음 푼 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix.reverse()
        print(matrix)

        for idx, arr in enumerate(matrix):
            # print(idx, arr)
            if arr[0] <= target:
                # print(arr[0])
                for num in matrix[idx]:
                    if num == target:
                        return True

        return False

# 효율적인 풀이
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 예외 처리
        if not matrix:
            return False

        # 첫 행의 맨 뒤
        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) - 1 and col >= 0:
            if target == matrix[row][col]:
                return True
            # 타겟이 작으면 왼쪽으로 이동
            elif target < matrix[row][col]:
                col -= 1
            # 타겟이 크면 아래로 이동
            elif target > matrix[row][col]:
                row += 1
        return False

# 파이썬다운 풀이
def searchMatrix(self, matrix, target):
    return any(target in row for row in matrix)