import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, 2*n + 1):
        if is_prime_num(i):
            cnt += 1
    print(cnt)