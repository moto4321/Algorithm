https://programmers.co.kr/learn/courses/4008

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

# zip
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = list(map(list, zip(*mylist)))


mylist = [1, 2, 3]
new_list = [40, 50, 60]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)



list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for number1, number2, number3 in zip(list1, list2, list3):
    print(number1 + number2 + number3)


animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}


# zip(2)
def solution(mylist):
    answer = []
    for number1, number2 in zip(mylist, mylist[1:]):
        answer.append(abs(number1 - number2))
    return answer

if __name__ == '__main__':
    mylist = [83, 48, 13, 4, 71, 11]    
    print(solution(mylist))

# 모든 멤버의 type 변환하기 - map
list1 = ['1', '100', '33']
list2 = list(map(int, list1))


# sequence 멤버를 하나로 이어붙이기 - join
my_list = ['1', '100', '33']
answer = ''.join(my_list)


# itertools를 사용하면, for문을 사용하지 않고도 곱집합을 구할 수 있습니다.
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))



# 2차원 리스트를 1차원 리스트로 만들기 - from_iterable
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))




# 순열과 조합 - combinations, permutations
import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기


# for 문과 if문을 한번에 - List comprehension의 if 문
# 파이썬의 list comprehension을 사용하면 한 줄 안에 for 문과 if 문을 한 번에 처리할 수 있습니다.
mylist = [3, 2, 6, 7]
answer = [number**2 for number in mylist if number % 2 == 0]



# flag 대신 for-else 사용하기
# 파이썬의 for-else 문을 사용하면 코드를 짧게 쓸 수 있고, 그 의미를 알아보기 쉽습니다.

import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')



# 두 변수의 값 바꾸기 - swap
# 파이썬에서는 다음과 같이 한 줄로 두 값을 바꿔치기할 수 있습니다.

a = 3
b = 'abc'

a, b = b, a # 참 쉽죠?



# 이진 탐색하기 - binary search
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))



# 가장 큰 수, inf
min_val = float('inf')
print(min_val > 10000000000) # True
# inf 에는 음수 기호를 붙이는 것도 가능
max_val = float('-inf')



# 파일 입출력 간단하게 하기
# 파이썬의 with - as 구문을 이용하면 코드를 더 간결하게 짤 수 있습니다. 코드를 아래와 같이 쓰면 다음과 같은 장점이 있습니다.

# 파일을 close 하지 않아도 됩니다: with - as 블록이 종료되면 파일이 자동으로 close 됩니다.
# readlines가 EOF까지만 읽으므로, while 문 안에서 EOF를 체크할 필요가 없습니다.
with open('myfile.txt') as file:
    for line in file.readlines():
        print(line.strip().split('\t'))