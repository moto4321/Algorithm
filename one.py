array = [3, 5, 1, 2, 4] # 5개의 데이터 (N = 5)
summary = 0

for x in array:
  summary += x

print(summary)

# 수행 시간은 데이터의 개수 N에 비례할 것임을 예측할 수 있다.
# 시간복잡도: O(N)

array = [3, 5, 1, 2, 4]

for i in array:
  for j in array:
    tmp = i * j
    print(tmp)


#시간 복잡도: O(N^2)
# 참고로 모든 2중 반복문의 시간 복잡도가 O(N^2)인 것은 아님
# 소스코드가 내부적으로 다른 함수를 호출한다면 그 함수의 시간 복잡도까지 고려해야함.

# 파이썬은 1초에 2천만번의 연산을 한다고 가정
# 코딩테스트의 시간제한은 대체로 1 ~ 5초까지


# 시간제한이 1초인 문제를 만났을 때, 일반적인 기준은 다음과 같다.
#N의 범위가 500인 경우: 시간복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 풀 수 있습니다.
#N의 범위가 2,000인 경우: 시간복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 풀 수 있습니다.
#N의 범위가 100,000인 경우: 시간복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있습니다.
#N의 범위가 10,000,000인 경우: 시간복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있습니다.

# 일반적인 알고리즘 문제 해결 과정은 다음과 같다
# 1. 지문 읽기 및 컴퓨터적 사고
# 2. 요구사항(복잡도) 분석
# 3. 문제해결을 위한 아이디어 찾기
# 4. 소스코드 설계 및 코딩

# 일반적으로 대부분의 문제 출제자들은 핵심 아이디어를 캐치한다면, 간결하게 소스코드를 작성할 수 있는 형태로 문제를 출제한다.

# 수행시간 측정
import time
start_time = time.time() # 측정 시작

# 프로그램 소스코드
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

#정수형
a = 10000
print(a)

a = -7
print(a)

a = 0
print(a)

#실수형
a = 1.2

# 지수표현 방식
# 1e9 = 10의 9제곱(1,000,000,000)


# 리스트 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)


n = 10
a = [0] * n
print(a)  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#리스트 컴프리헨션
array = [i for i in range(10)]
print(array) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i  in range(20) if i % 2 == 1]
print[array]

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print[array]

# 코드 1: 리스트 컴프리헨션
array = [i for i in range(20) if i % 2 == 1] # 한줄로 작성 가능
print(array)

# 코드 2: 일반적인 코드
array = []
for i in range(20):
  if i % 2 == 1:
    array.append(i)

print(array)

# 리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있습니다.
# 특히 N x M 크기의 2차원 리스트를 한 번에 초기화 해야 할 때 매우 유용합니다.
  # 좋은 예시 
  array = [[0] * m for _ in range(n)]

# 만약 2차원 리스트를 초기화할 때 다음과 같이 작성하면 예기치 않은 결과가 나올 수 있습니다.
  # 잘못된 예시
  array = [[0] * m] * n
  #위 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식됩니다.

# 파이썬에서 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 사용한다.
  # 코드 1: 1부터 9까지의 자연수를 더하기
  summary = 0
  for i in range(1, 10):
    summary += i
  print(summary)

  # 코드 2: "Hello World"를 5번 출력하기
  for _ in range(5):
    print("Hello World")

# 리스트 관련 기타 메서드
append()
sort()
reverse()
insert()
count()
remove()

a = [1, 4, 3]
print("기본 리스트: ", a)  # 기본 리스트: [1, 4, 3]

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)  # 삽입: [1, 4, 3, 2]

# 오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)  # 오름차순 정렬: [1, 2, 3, 4]

# 내림차순 정렬
a.sort(reverse = True)
print("내림차순 정렬: ", a)   # 내림차순 정렬: [4, 3, 2, 1]



a = [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)     # 원소 뒤집기: [1, 2, 3, 4]

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)     # 인덱스 2에 3추가: [1, 2, 3, 3, 4]

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))     # 값이 3인 데이터 개수: 2

# 특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)        # 값이 1인 데이터 삭제: [2, 3, 3, 4]



# 리스트에서 특정 값을 가지느 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5} # 집합 자료형 (집합 자료형은 추후에 다시 다룹니다.)

# remove_list 에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)   #[1, 2, 4]  



# 문자열 자료형
  # 문자열 변수를 초기화 할때는 ""와 ''를 이용
  # 문자열 안에 ""나 ''가 포함되어야 하는 경우가 있다.
    # 전체 문자열을 ""로 구성하는 경우, 내부적으로 ''를 포함할 수 있다.
    # 전체 문자열을 ''로 구성하는 경우, 내부적으로 ""를 포함할 수 있다.
    # 혹은 (\)를 사용하면, ""나 ''를 원하는 만큼 포함시킬 수 있다.

data = 'Hello World'
print(data)   # Hello World

data = "Don't you know \"Python\"?"
print(data)   # Don't you know "Python"?


# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)    # Hello World

a = "String"
print(a * 3)    # StringStringString

a = "ABCDEF"
print(a[2 : 4])   # CD


# 튜플 자료형
  # 튜플 자료형은 리스트와 유사하지만 다음과 같은 문법적 차이가 있다.
  # 튜플은 한 번 선언된 값을 변경할 수 없다.
    # 리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용한다.
    # 튜플은 리스트에 비해 상대적으로 공간 효율적이다.(더 적은 양의 메모리 사용)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 네 번째 원소만 출력
print(a[3])   # 4

# 두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])   #(2, 3, 4)

# 튜플을 사용하면 좋은 경우
  # 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
    # 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용한다.
  # 데이터의 나열을 해싱(Hashing)의 키 값으로 사용해야 할 때
    # 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있다.
  # 리스트보다 메모리를 효율적으로 사용해야 할 때



# 사전 자료형
  # 사전 자료형은 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형.
    # 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비됨
  # 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 불가능한(Immutable) 자료형'을 키로 사용 할 수 있음
# 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이요하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

// { '사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut', }
// '사과를 키로 가지는 데이터가 존재한다'


# 사전 잘형 관련 메소드
  # 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 메소드를 지원함
    # 키 데이터만 뽑아서 리스트로 이용할 때는  keys() 함수를 이용
    # 값 데이터만 봅아서 리스트로 이용할 때는 values() 함수를 이용

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
  print(data[key])



a = dict()
a['홍길동'] = 97
a['이순신'] = 98

print(a)

b = {
  '홍길동': 97,
  '이순신': 98
}

print(b)

key_list = b.keys()   # 키값만을 가져오도록
key_list = list(b.keys())   # 실제로는 list함수로 형변환을 해준다.
print(key_list)  


# 집합 자료형
  # 집합은 다음과 같은 특징이 있다.
    # 중복을 허용하지 않는다.
    # 순서가 없다.
  # 집합은 리스트 혹은 문자열을 이용해서 초기화할 수 있다.
    # 이 때 set() 함수를 이용한다.
  # 혹은 중괄호({}) 안에 각 원소를 콤마(,)를 기준으로 구분하여 삽입함으로써 초기화 할 수 있다.
  # 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 할 수 있다.


# 집합 자료형 초기화 방법 1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)   # {1, 2, 3, 4, 5}

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)   # {1, 2, 3, 4, 5}

# 집합 자료형의 연산
  # 기본적인 집합 연산으로는 합집합, 교집합, 차집합 연산 등이 있다.
    # 합집합: 집합 A에 속하거나 B에 속하는 원소로 이루어진 집합.
    # 교집합: 집합 A에도 속하고 B에도 속하는 원소들로 이루어진 집합.
    # 차집합: 집합 A의 원소 중에서 B에 속하지 않는 원소들로 이루어진 집합


a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)   #{1, 2, 3}

# 새로운 원소 추가
data.add(4)
print(data)   # {1, 2, 3, 4}

# 새로원 원소 여러 개 추가
data.update(5, 6)
print(data)   # {1, 2, 3, 4, 5, 6}

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)   # {1, 2, 4, 5, 6}


# 사전 자료형과 집합 자료형의 특징
  # 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있다.
  # 사전 자료형과 집합 자료형은 순서가 ㅇ벗기 때문에 인덱싱으로 값을 얻을 수 없다.
    # 사전의 키(Key) 혹은 집합의 원소(Element)를 이용해 O(1)의 시간 복잡도로 조회.


# 기본 입출력 1:19:31
  # 모든 프로그램은 적절한 (약속된) 입출력 양식을 가지고 있다.
  # 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것.
  
# 자주 사용되는 표준 입력 방법
  input() # 한 줄의 문자열을 입력 받는 함수
  map() # 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
  # ex) 공백을 기준으로 구분된 데이터를 입력 받은 때는 다음과 같이 사용
    list(map(int, input().split()))
  # ex) 공백을 기준으로 구분된 데이터가 많지 않다면, 단순히 다음과 같이 사용
    a, b, c = map(int, input().split())



# 입력을 위한 전형적인 소스코드 1)
  # 데이터의 개수 입력
  n = int(input())
  # 각 데이터를 공백을 기준으로 구분하여 입력
  data = list(map(int, input().split()))

  data.sort(reverse=True)
  print(data)

# 입력을 위한 전형적인 소스코드 2)
  # n, m, k를 공백을 기준으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 빠르게 입력받기
  # 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우가 있다.
  # 파이썬의 경우 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드를 이용
    # 단, 입력 후 엔터(Enter)가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용

import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)


# 자주 사용되는 표준 출력 방법
  # 파이썬에서 기본 출력은 print() 함수를 이용
    # 각 변수를 콤마(,)를 이용하여 띄어쓰기로 구분하여 출력할 수 있다.
  # print()는 기본적으로 출력 이후에 줄 바꿈을 수행
    # 줄 바꿈을 원치 않는 경우 'end' 속성을 이용할 수 있다.

# 출력을 위한 전형적인 소스코드
  # 출력할 변수들
a = 1
b = 2
print(a, b)
print(7, end=" ") 
print(8, end=" ")

# 출력할 변수
answer = 7
print(" 정답은 " + str(answer) + "입니다.")

# f-string 예제
  # 파이썬 3.6부터 사용 가능하며, 문자열 앞에 접두사 'f'를 붙려 사용
  # 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있다.

  answer = 7
  print(f"정답은 {answer}입니다.")    # 정답은 7입니다.


# 조건문과 반복문 1:29:13

# 조건문
  # 조건문은 프로그매의 흐름을 제어하는 문법
  # 조건문을 이용해 조건에 따라서 프로그램의 로직을 설정할 수 있다.

# 조건문 예제
x = 15

if x >= 10:
  print("x >= 10")

if x >= 0:
  print("x >= 0")

ir x >= 30:
  print("x >= 30")


# 파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)

score = 85

if score >= 70:
  print('성적이 70점 이상입니다.')
  if score >= 90:
    print('우수한 성적입니다.')
else:
  print('성적이 70점 미만입니다.')
  print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')


# 탭을 사용하는 쪽과 공백 문자(space) 를 여러 번 사용하는 쪽으로 두 진영이 있다.
  # 이에 대한 논쟁은 지금까지도 활발하다.
# 파이썬 스타일 가이드라인에서는 4개의 공백 문자를 사용하는 것을 표준으로 설정

# 조건문의 기본적인 형태는 if ~ elif ~ else 이다.
  # 조건문을 사용할 때 elif 혹은 else 부분은 경우에 따라서 사용하지 않아도 된다.

if 조건문 1:
    조건문 1이 True 일 때 실행되는 코드
elif 조건문 2:
    조건문 1에 해당하지 않고, 조거문 2가 True 일때 실행되는 코드
else
    위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드



# 비교 연산자
  # 비교 연산자는 특정한 두 값을 비교할 때 이용할 수 있다.
    # 대입 연산자(=)와 같음 연산자(==)의 차이점에 유의하라.

X == Y  # X와 Y가 서로 같을 때 참(True)이다.
X != Y  # X와 Y가 서로 다를 때 참(True)이다.
X > Y   # X가 Y보다 클 때 참(True)이다.
X < Y   # X가 Y보다 작을 때 참(True)이다.
X >= Y  # X가 Y보다 크거나 같을 때 참(True)이다.
X <= Y  # X가 Y보다 작거나 같을 때 참(True)이다.


# 논리 연산자
  # 논리 연산자는 논리 값(True/False) 사이의 연산을 수행할 때 사용

X and Y  # X와 Y가 모두 참(True)일 때 참(True)이다.
X or Y   # X와 Y 중에 하나만 참(True)이어도 참(True)이다.
not X    # X가 거짓(Flase)일 때 참(True)이다.


# 파이썬의 기타 연산자
  # 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공됨.
    # 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용이 가능.

x in 리스트      # 리스트 안에 x가 들어가 있을 때 참(True)이다.
x not in 리스트  # 리스트 안에 x가 들어가 있지 않을 때 참(True)이다.


# 파이썬의 pass 키워드
  # 아무것도 처리하고 싶지 않을 때 pass 키워드를 사용
  
  # ex) 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우

score = 85

if score >= 80:
    pass # 나중에 작성할 코드
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')


# 조건문의 간소화
  # 조건문에서 실행될 소스코드가 한 줄인 경우

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

# 조건문 표현식(Conditional Exression)은 if ~ else 문을 한 중에 작성할 수 있도록 해줌

score = 85

result = "Success" if score >= 80 else "Fail"

print(result)


# 파이썬 조건문 내에서의 부등식
  # 다른 프로그래밍 언어와 다르게 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다.
  # ex) x > 0 and x < 20 과 0 < x < 20은 같은 결과를 반환

# 코드스타일1
x = 15
if x > 0 and x < 20:
    print("x는 0 이상 20 미만의 수입니다.")

# 코드스타일2
x = 15
if 0 < x < 20:
    print("x는 0 이상 20 미만의 수입니다.")

# 본 책에서는 다른 언어를 다룰 때 헷갈리지 않도록 x > 0 and x < 20 와 같이 비교 연산자 사이에 and, or 등의 연산자가 들어가는 형태의 코드를 이용.


# 반복문
  # 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법
  # 파이썬에서는 while문과 for문이 있는데, 어떤 것을 사용해도 상관 없음.
    # 다만 코딩테스트에서의 실제 사용예시를 확인해보면, for문이 더 간결한 경우가 많음,

# 1부터 9까지 모든 정수의 합 구하기 예제(while문)

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result) # 45

# 1부터 9까지 홀수의 합 구하기 예제(while문)

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result) # 25

# 반복문에서의 문한 루프
  # 무한 루프(Infinite Loop)란 끊임없이 반복되는 반복 구문을 의미
    # 코딩 테스트에서 무한 루프를 구현할 일은 거의 없으니 유의
    # 반복문을 작성한 뒤에는 항상 반복문을 탈출할 수 있는지 확인

x = 10

while x > 5:
    print(x)


# 반복문: for문
  # 반복문으로 for문을 이용할 수도 있다.
  # for문의 구조는 다음과 같은데, 특정한 변수를 이용하여 'in'뒤에 오는 데이터(리스트, 튜플 등)에 포함 되어있는 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문

for 변수 in 리스트:
    실행할 소스코드


#
array = [9,8,7,6,5]

for x in array:
    print(x)


# for문에서 연속적인 값을 차례대로 순회할 때는 range()를 주로 사용한다.
  # 이 때 range(시작 값, 끝 값 + 1)형태로 사용
  # 인자를 하나만 넣으면 자동으로 시작 값은 0이 됨

result = 0

# i는 1부터 9까지의 모든 값을 조회
for i in range(1, 10):
    result += i

print(result) # 45

# 1부터 30까지 모든 정수의 합
result = 0

for i in range(1, 31)
    result += i

print(result) 

# 파이썬의 continue 키워드
  # 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때 continue를 사용
  # 1부터 9까지의 홀수의 합을 구할 때 다음과 같이 작성할 수 있다.

result = 0

for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += i

print(result) # 25


# 파이썬의 break 키워드
  # 반복문을 즉시 탈출하고자 할 때 break를 사용
  # 1부터 5까지의 정수를 차례대로 출력하고자 할 때 다음과 같이 작성 가능

i = 1

while True:
    print("현재 i의 값:", i)
    if i == 5:
        break
    i += 1

# 
scores = [90, 85, 77, 65, 97]

for i in range(5):  # i를 0부터 4까지
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 1번 학생은 합격입니다.
# 2번 학생은 합격입니다.
# 5번 학생은 합격입니다.


# 특정 번호의 학생은 제외
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")


# 1번 학생은 합격입니다.
# 5번 학생은 합격입니다. 


for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()

# 함수와 람다 표현식
  # 함수
    # 함수란 특정한 작업을 하나의 단위로 묶어놓은 것을 의미
    # 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있다.

  # 내장함수 : 파이썬이 기본적으로 제공하는 함수
  # 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

  # 매개변수 : 함수 내부에서 사용할 변수
  # 반환 값 : 함수에서 처리된 결과를 반환

def 함수명(매개변수):
    실행할 소스코드
    return 반환 값


# 더하기 함수 예시 1)
def add(a, b):
    return a + b

print(add(3, 7))

# 더하기 함수 예시 2)
def add(a, b):
    print('함수의 결과:', a + b)

add(3, 7)


# 파라미터 지정하기 
  # 파라미터의 변수를 직접 지정할 수 있다.
    # 이 경우 매개변수의 순서가 달라도 상관 없다.

def add(a, b):
    print('함수의 결과:', a + b)

add(b = 3, a = 7)


# global 키워드
  # global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조

a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a) 


# 여러개의 반환 값
  # 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있다.

def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)

# 람다 표현식
  # 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있다.
    # 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징

def add(a, b):
    return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))


# 람다 표현식 예시: 내장함수에서 자주 사용되는 람다 함수

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# 람다 표현식 예시: 여러 개의 리스트에 적용

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))  # [7, 9, 11, 13, 15]

# 실전에서 유용한 표준 라이브러리
  # 내장함수
  # itertools: 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능들을 제공, 특히 순열과 조합 라이브러리는 코딩테스트에서 자주 사용
  # heapq: 힙(Heap) 자료구조를 제공, 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
  # bisect: 이진 탐색(Binary Search) 기능을 제공
  # collections: 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함
  # math: 필수적인 수학적 기능을 제공, 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수를 포함


# sum()
result = sum([1, 2, 3, 4, 5])
print(result)  # 15

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result) # 2 7

# eval
result = eval("(3+5)*7")
print(result) # 56



# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)           # [1, 4, 5, 8, 9]
print(reverse_result)   # [9, 8, 5, 4, 1]

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result) # [('홍길동', 35),('아무개', 74), ('이순신', 32)]

# 순열과 조합
  순열의 수: nPr
  조합의 수: nCr

# 순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
  # {'A', 'B', 'C'}

from itertools import permutations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(permutations(data, 3))
print(result)

# 조합: 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것 
  # {'A', 'B', 'C'}

from intertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)


# 중복 순열
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# 중복 조합
from intertools import combinations_with_replacement

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations_with_replacement(data, 2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)


# Counter
  # 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공
  # 리스트와 같은 반복 가능한(iterable) 객체가 주어졌을 때 내부의 원소가 몇번씩 등장했는지를 알려줌

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력      # 3
print(counter['green']) # 'green'이 등장한 횟수 출력    # 1
print(dict(counter)) # 사전 자료형으로 반환             # {'red': 2, 'blue': 3, 'green': 1}


# 최대 공약수와 최소 공배수
  # 최대 공약수를 구해야 할 때 math 라이브러리의 gcd() 함수를 이용할 수 있음

import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산 # 7
print(lcm(21, 14))      # 최소 공배수(LCM) 계산 # 42