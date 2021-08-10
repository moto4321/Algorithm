N = 1264
K = 3
count = 0

while True:
    if N % K == 0:
        N /= K
        if N == 0:
            
        count += 1
    else:
        N -= 1
        count += 1
print(count)
