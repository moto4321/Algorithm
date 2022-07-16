# 캠핑
case = 0
while True:
    answer = 0
    l, p, v = map(int, input().split()) 
    # 5, 8, 20
    # 연속하는 8일 중 5일 동안만 사용할 수 있고 강산이는 이제 막 20일짜리 휴가를 시작했다
    if l == 0 and p == 0 and v == 0:
        break
    case += 1
    answer = v // p * l
    left = v % p
    if left <= l:
        answer += left
    else:
        answer += l
    print(f"Case {case}: {answer}")