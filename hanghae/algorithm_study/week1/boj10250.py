# ACM 호텔

t = int(input())
for _ in range(t):
    # 층 수, 층 방 수, 몇 번째 손님
    h, w, n = map(int, input().split())
    if n % h == 0:
        y = h
        x = n // h
    else:
        y = n % h
        x = n // h + 1
    print(y * 100 + x)