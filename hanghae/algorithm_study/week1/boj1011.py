# Fly me to the Alpha Centauri
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = abs(x - y)
    num = 1
    while True:
        if n * (n + 1) >= dist:
            break
        n += 1

    if n**2 < dist:
        print(n * 2)
    else:
        print(n * 2 - 1)
