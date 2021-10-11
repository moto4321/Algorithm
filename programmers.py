# divmod
a = 7
b = 5
print(divmod(a, b))

# int(num, base) 진법변환
num = '3212'
base = 5
answer = int(num, base)

# ljust / center / rjust
s = '가나다라'
n = 7

s.ljust(n) # 좌측 정렬
s.center(n) # 가운데 정렬
s.rjust(n) # 우측 정렬

# string 모듈
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789

# sorted
list1 = [3, 2, 1]
list2 = sorted(list1)