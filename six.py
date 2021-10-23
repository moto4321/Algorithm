# 피보나치 수열
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4)) # 네번째 피보나치수열 호출 # 3

# 하지만 O(2^n) 시간복잡도를 가지기 때문에 f(100) 만 하더라도 시간이 오래걸림
# 따라서 다이나믹 프로그래밍이 필요함
# 사용 조건
# 1. 최적부분 구조: 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 중복되는 부분 문제: 동일한 작은 문제를 반복적으로 해결합니다.
# 피보나치 수열은 다이나믹 프로그래밍의 사용조건을 만족

# 탑다운 vs 바텀업

# 한 번 계산된 결과를 메모리제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))


# 바텀업 방식
# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 (바텀업 다이나믹 프로그래밍)
for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])


# 개미전사
n = int(input())
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(바텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])