# 시간 초과
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))
top = max(lst)
cnt = 0

cnt_lst = []
for i in range(0, n - x + 1):
    sum = 0
    for j in range(i, i + x):
        sum += lst[j]
    cnt_lst.append(sum)

if max(cnt_lst) == 0:
    print('SAD')
else:
    print(max(cnt_lst))
    print(cnt_lst.count(max(cnt_lst)))



# 정답 코드
import sys
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

if max(data) == 0:
    print('SAD')
else:
    # value 초기화
    value = sum(data[:x]) # x개씩 나눠서 sum
    max_value = value
    max_cnt = 1

    for i in range(x, n):
        # 슬라이딩 윈도우 진행
        value += data[i]
        # print("+", data[i])
        value -= data[i - x] # 슬라이딩 윈도우 뒤에 값
        # print("-", data[i - x])

        # value의 최대값 찾음
        if value > max_value:
            max_value = value
            max_cnt = 1
        
        # 최대값 count
        elif value == max_value:
            max_cnt += 1

    print(max_value)
    print(max_cnt)