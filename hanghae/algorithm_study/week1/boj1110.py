# 더하기 사이클
n = int(input()) # 26
cnt = 0
target = n
while True:
    first = target // 10
    second = target % 10
    cnt += 1

    num = first + second
    if num >= 10:
        new_num = second*10 + (num % 10)
    else:
        new_num = second*10 + num

    if new_num == n:
        print(cnt)
        break

    target = new_num