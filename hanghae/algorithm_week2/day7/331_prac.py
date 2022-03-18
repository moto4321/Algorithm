# 섬의 개수
# leetcode 200

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]


# 스택을 이용한 풀이
def numIslands(grid):
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    cnt = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != '1':
                continue

            cnt += 1

            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == '0':
                        continue
                    stack.append((nx, ny))

    return cnt


# 재귀를 이용한 풀이
def island_dfs_recursive(grid):
    # 북, 동, 남, 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    rows = len(grid)
    cols = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        # 방문 처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(rows):
        for c in range(cols):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt







