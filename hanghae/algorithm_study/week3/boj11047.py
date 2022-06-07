# 동전 0
n, k = map(int, input().split())
coin_lst = []
for _ in range(n):
    coin_input = int(input())
    coin_lst.append(coin_input)

new_lst = sorted(coin_lst, reverse=True)

idx = 0 # 여기서 시작하는 동전부터 나눌것임
for i, coin in enumerate(new_lst):
    if coin < k:
        idx = i
        break

answer = 0
rest = 0
for i in range(idx, len(coin_lst)):
    answer += k // new_lst[i]
    rest = k % new_lst[i]
    k = rest
    if rest == 0:
        break

print(answer)

# 정답 풀이
N, K = map(int, input().split())
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)