n = int(input())

cnt = n // 5
rst = n % 5
if rst == 0:
    print(cnt)
else:
    # rst 1 ~ 4 
    if rst == 3:
        print(cnt + 1)
    else:
        if n % 3 == 0:
            print(n // 3)
        else:
            print(-1)