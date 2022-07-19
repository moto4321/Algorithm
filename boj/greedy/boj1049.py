# 기타줄
n, m = map(int, input().split())
string_price = []
for _ in range(m):
    a, b = map(int, input().split())
    string_price.append((a, b))

min_price = 100000
for price in string_price:
    # 패키지로 살때 , 몇개를 사야하는지
    cnt = n // 6
    rest = n % 6
    if rest != 0:
        cnt += 1
    
    min_price = min(min_price, price[0] * cnt)
    # 낱개로 살때
    min_price = min(min_price, price[1] * n)
    

print(min_price)

# 정답
n, m =map(int, input().split())

answer = 0
price_list = []

for _ in range(m):
    price = tuple(map(int, input().split()))
    price_list.append(price)

six_list = sorted(price_list, key=lambda x: x[0])
one_list = sorted(price_list, key=lambda x: x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    answer = six_list[0][0]
    if six_list[0][0] < one_list[0][1] * (n % 6):
        answer = six_list[0][0] * (n // 6 + 1)
else:
    answer = one_list[0][1] * n

print(answer)