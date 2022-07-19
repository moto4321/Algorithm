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
n, m = map(int, input().split())

result = 0
six_list = []
one_list = []
for _ in range(m):
    a, b = map(int, input().split())
    six_list.append(a)
    one_list.append(b)

six_list.sort()
one_list.sort()

if six_list[0] <= one_list[0] * 6:
    result = six_list[0] * (n // 6) + one_list[0] * (n % 6)
    if six_list[0] < one_list[0] * (n % 6):
        result = six_list[0] * (n // 6 + 1)
else:
    result = one_list[0] * n

print(result)