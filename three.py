# 그래프 탐색 알고리즘: DFS/BFS
  # 탐색(Search)이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 말한다.
  # 대표적인 그래프 탐색 알고리즘으로는 DFS와 BFS가 있다.
  # DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이므로 반드시 숙지해야한다. (국내 대기업에서 DFS와 BFS를 적절히 활용해야하는 문제가 자주 출제)

# 스택 자료구조
  # 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조이다.
  # 입구와 출구가 동일한 형태로 스택을 시각화할 수 있다.

# 프링글스 과자통!

# 스택 구현 예제(Python)
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력    [1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력          [5, 2, 3, 1]



# 큐 자료구조
  # 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
  # 큐는 입구와 출구가 모두 뚫려있는 터널과 같은 형태로 시각화 할 수 있다.

  # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
  # [4, 1, 7, 3]

# 큐 구현 예제(Python)
from collections import deque  # list 자료형을 이용할 경우 시간복잡도가 높다 따라서 queue를 이용할 경우 deque생성 후 사용

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력  [3, 7, 1, 4]
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력  [4, 1, 7, 3]



# 재귀 함수
  # 재귀 함수(Recursive Function)란 자기 자신을 다시 호출하는 함수를 의미
  # 단순한 형태의 재귀 함수 예제
    # '재귀 함수를 호출합니다.'라는 문자열을 무한히 출력
    # 어느 정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

