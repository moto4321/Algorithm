# 암호 만들기

# 내 풀이
# 4 6
# a t c i s w
l, c = map(int, input().split()) # 4 6
letters = list(input().split())
vowels = ['a', 'e', 'o', 'i', 'u']
result = []
vo_cnt = 0
not_vo = 0
def dfs(index, path): # (0, '')
    if len(path) == l:
        vo_cnt = 0
        not_vo = 0
        path = sorted(path)
        for each in path:
            if each in vowels:
                vo_cnt += 1
            else:
                not_vo += 1

            if path not in result and vo_cnt > 0 and not_vo > 1:
                result.append(path)
        return

    for i in range(index, c): # i=0 index=0 c=6
        for j in letters[i]:     # 'a'
            dfs(i + 1, path + j) # (1, 'a')


dfs(0, '')


for i in range(len(result)):
    result[i] = ''.join(result[i])

result.sort()
for answer in result:
    print(answer)


# combinations를 이용(답은 똑같이 나오는데 '출력 초과'라고 뜸)
letters = list(input().split())
vowels = ['a', 'e', 'i', 'u', 'o']
vo_cnt = 0

from itertools import combinations

result = []
answer = []

word_list = list(combinations(letters, 4))
for word in word_list:
    result.append(''.join(sorted(word)))

for word in result:
    vo_cnt = 0
    for each in word:
        if each in vowels:
            vo_cnt += 1

    if vo_cnt > 0 and vo_cnt < l - 1 and word not in answer: # l - 1
        answer.append(word)

answer.sort()
for ans in answer:
    print(ans)