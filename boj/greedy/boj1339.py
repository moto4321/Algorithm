# 단어 수학
n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

lst.sort(reverse=True, key=len)

alpha = []
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = []
for each in lst:
    alpha = []
    for string in each:
        if string not in alpha:
            alpha.append((string, max(num_list)))
            num_list.remove(max(num_list))
    num = ''
    for j in alpha:
        num += str(j[1])
    result.append(num)

# print(result)
answer = 0
for i in result:
    answer += int(i)

print(answer)




# 정답 풀이
N=int(input())

# 입력할 단어 변수 선언
words = []

# 입력받기
for _ in range(N):
  words.append(input())

# 딕셔너리 초기화
dict = {}

# 딕셔너리에 알파벳별로 값을 집어 넣어준다.
for word in words:
  # 길이를 계산하여 10^square_root만큼 넣어주기 위해
  # -1를 하는 이유는 맨뒤는 1의자리이기 때문에
  # 0 제곱을 해야 한다.
  square_root = len(word) - 1
  for c in word:
    if c in dict: # 값이 있는경우 더해준다.
      dict[c] += pow(10, square_root)
    else: # 없는경우 그대로 넣어준다.
      dict[c] = pow(10, square_root)
    # 제곱근을 뺴준다.
    square_root -= 1 

# 딕셔너리를 큰값부터 쓰기 위해 정렬
dict = sorted(dict.values(), reverse=True)

# 값 계산할 변수 선언
result,m = 0,9

# 값 계산하기
for value in dict:
  result += value * m
  m -= 1

print(result)