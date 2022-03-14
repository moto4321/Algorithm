class Solution:
    def removeDuplicateLetters(self, s: str) -> str:


        d = {char: idx for idx, char in enumerate(s)}

        """
        Input = "cbacdcbc"

        {"c" : 7, "b" : 6, "a" : 2, "d" : 4}

        Input = "bcabc"

        {'b': 3, 'c': 4, 'a': 2}

        """

        print(d)

        res = []
        for idx, char in enumerate(s): # idx = 2 char = 'a' res = ['b', 'c']
            if char not in res:
                # res가 비어있지 X AND
                # 마지막의 요소는 뒤에서 한 번 더 나타난다는 보장 있는 경우
                # 마지막의 요소보다 char의 우선순위가 높은 경우
                # -> 마지막 요소 pop
                while res and idx < d[res[-1]] and char < res[-1]:
                    res.pop() # res = []
                res.append(char) # res = ['a', 'b', 'c']


        return "".join(res)