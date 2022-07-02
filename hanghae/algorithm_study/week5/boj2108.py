# 통계학
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort()

# 산술평균
print(round(sum(lst) / n))
# 중앙값
print(lst[len(lst) // 2])
# 최빈값
temp = [lst[0]]
last = lst[0]
# 현재 숫자 개수를 세는 변수
cnt = 1
# 최빈값에 해당하는 개수 변수
high = 0
# idx = 0
for num in lst[1:]:
    # 이전 숫자와 현재 숫자가 불일치
    if num != last:
        # 특정 수의 개수가 현재 최빈값 개수보다 많다면
        if cnt > high:
            # 최빈값 리스트 초기화
            highs = []
            # 최빈값 리스트에 추가
            highs.append(last)
            high = cnt
        # 특정 수의 개수가 현재 최빈값 개수와 같다면 최빈값 추가
        elif cnt == high and last not in highs:
            highs.append(last)
        cnt = 1
    # 중복된 수가 존재한다면 cnt 개수 추가
    else:
        cnt += 1
    last = num

# 마지막 수 계산
if cnt > high:
    highs = [last]
elif cnt == high and last not in highs:
    highs.append(last)

# 최빈값이 1개라면 단일값 출력
if len(highs) == 1:
    print(highs[0])
# 최빈값이 여러개라면 두 번째로 작은 값 출력
else:
    print(highs[1])

# 범위
print(max(lst) - min(lst))