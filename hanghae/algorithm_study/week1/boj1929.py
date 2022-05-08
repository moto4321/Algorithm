# 소수 구하기
import math
import sys
input = sys.stdin.readline
m, n = map(int, input().split())

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True

def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

for i in range(m, n + 1):
    if isPrime(i):
        print(i)