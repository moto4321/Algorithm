# 정수 삼각형

# 어렵다...
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

INF = int(1e9)
temp = [[INF] * i for i in range(1, n + 1)]

temp[0][0] = tri[0][0]

def dp(r, c):
    if not(0 <= r < n and 0 <= c < len(tri[r])):
        return 0

    if temp[r][c] != INF:
        return temp[r][c]

    temp[r][c] = tri[r][c] + max(dp(r - 1, c - 1), dp(r - 1, c))
    return temp[r][c]

for col in range(n):
    dp(n - 1, col)

print(max(temp[n - 1]))

