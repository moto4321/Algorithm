class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        """
        Input = "cbacdcbc"

        {"c" : 7, "b" : 6, "a" : 2, "d" : 4}

        """

        d = {char: idx for idx, char in enumerate(s)}

        print(d)

        res = []

        for idx, char in enumerate(s):
            if char not in res:
                # res가 비어있지 X AND
                # 마지막의 요소는 뒤에서 한 번 더 나타난다는 보장 있는 경우
                # 마지막의 요소보다 char의 우선순위가 높은 경우
                # -> 마지막 요소 pop
                while res and idx < d[res[-1]] and char < res[-1]:
                    res.pop()
                res.append(char)

        return "".join(res)