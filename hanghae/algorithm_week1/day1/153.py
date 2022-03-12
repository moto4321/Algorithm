# 그룹 애너그램

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_strs = []
        temp = []
        for word in strs:
            # sort() vs sorted()
            sort_word = sorted(word)
            sort_word = ''.join(sort_word)  # 알파벳 순으로 정렬
            new_strs.append(sort_word)  # result라는 배열에 저장 []
            if sort_word not in temp:
                temp.append(sort_word)

        # strs = ["eat","tea","tan","ate","nat","bat"]
        # new_strs = ['aet', 'aet', 'ant', 'aet', 'ant', 'abt']
        # temp = ['aet', 'ant', 'abt']

        answer = [[] for _ in range(len(temp))]

        for i in range(len(strs)):
            for j in range(len(temp)):
                if new_strs[i] == temp[j]:
                    answer[j].append(strs[i])

        return answer





class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())