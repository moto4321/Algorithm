import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = {}

for _ in range(n):
    site, pw = input().split()
    data[site] = pw

for _ in range(m):
    input_site = input().rstrip()
    print(data[input_site])

# 그냥 input값을 쓸 경우 시간 초과가 난다.

# 기본적으로 readline()은 개행문자(줄 바꿈 문자)를 포함하고 있습니다.
# 그래서 문자열 마지막에 개행문자가 포함되어 출력되는데 이러한 공백 없이 출력할 수 있게 하는 함수가 있습니다.
