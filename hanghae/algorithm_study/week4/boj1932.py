# 정수 삼각형
n = int(input())
tri = []
for _ in range(n):
    line = list(map(int, input().split()))
    tri.append(line)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            tri[i][j] = tri[i - 1][j] + tri[i][j]
        elif j == len(tri[i]) - 1:
            tri[i][j] = tri[i - 1][j - 1] + tri[i][j]
        else:
            tri[i][j] = max(tri[i - 1][j - 1] + tri[i][j], tri[i - 1][j] + tri[i][j])

# print(tri)
print(max(tri[n - 1]))