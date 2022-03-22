# 1, 2, 3 더하기
t = int(input())
result = []

def dfs(num, sum):  # (4, 0)
    global count
    # 더한 값이 구하는 값보다 크다면 return
    if num < sum:
        return

    # 더한 값이 구한 값과 같다면 개수 추가
    if num == sum:
        count += 1
        return

    for i in range(1, 4): # 1, 2, 3 # i = 1
        sum += i                    # sum = 1
        # dfs 재귀적 수행
        dfs(num, sum)           # dfs(4, 1)
        sum -= i


# 입력받고 dfs 메서드 수행
for _ in range(t):
    num = int(input()) # 4
    count = 0
    dfs(num, 0)
    result.append(count)

# 결과 출력
for answer in result:
    print(answer)