a, b, c = map(int, input().split())

cnt = 0

while True:
    cnt += 1
    if a + b*cnt < c*cnt:
        print(cnt)
        break
    