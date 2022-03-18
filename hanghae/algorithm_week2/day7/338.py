# 전화번호 문자 조합
# leetcode 17

# 리스트 컴프리헨션
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if digits == "":
            return []

        numbers = list(phone_map[digits[0]])
        # ['a', 'b', 'c']

        for digit in digits[1:]:
            # 다음과 같이 이중 for문을 한줄로 작성 가능하다.
            numbers = [old + new for old in numbers for new in list(phone_map[digit])]

        return numbers

# 재귀를 이용한 풀이

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return

            # 입력값 자릿수 단위반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

    if not digits:
        return []

    dic = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    result = []
    dfs(0, "")

    return result





