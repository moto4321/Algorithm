# N - Queen

# 내 풀이(시간이 애매하다)
n = int(input())

visited = [-1] * n
cnt = 0

def is_ok_on(nth_row):
    for row in range(nth_row):
        if visited[row] == visited[nth_row] or nth_row - row == abs(visited[nth_row] - visited[row]):
            return False
    return True

def dfs(row):
    global cnt
    if row >= n:
        cnt += 1
        return

    for col in range(n):
        visited[row] = col
        if is_ok_on(row):
            dfs(row + 1)

dfs(0)
print(cnt)



# 최적화한 풀이!!(안정적으로 통과) - 아직 연습이 필요함
def backTracking(rowPos):
    global answer

    # 퀸을 모두 배치했다면 끝
    if rowPos == n:
        answer += 1
        return

    for col in range(n):
        flag = True
        # 이전 행들에 대해서
        for row in range(rowPos):
            # 같은 열에 위치해있거나 대각선에 퀸이 이미 존재한다면 가지치기
            if queenLocation[row] == col or rowPos - row == abs(col - queenLocation[row]):
                flag = False
                break
        if flag:
            queenLocation[rowPos] = col
            backTracking(rowPos + 1)


n = int(input())
answer = 0
# 각 row마다 queen이 위치하는 인덱스를 저장하는 리스트
queenLocation = [0] * n
backTracking(0)
print(answer)