# 프로그래머스 방문 길이

def solution(dirs):
    answer = 0
    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    d = {
        "U": 0,
        "R": 1,
        "D": 2,
        "L": 3
    }

    visited = set()
    answer = 0
    x, y = 0, 0

    for dir in dirs:
        i = d[dir]
        nx = x + dx[i]
        ny = y + dy[i]
        if abs(nx) > 5 or abs(ny) > 5:
            continue
        if (x, y, nx, ny) not in visited:
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            answer += 1

        x, y = nx, ny

    return answer