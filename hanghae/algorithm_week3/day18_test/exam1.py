# 프로그래머스 H-Index

# 내 풀이
def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    lst = sorted([i for i in range(max(citations))], reverse=True)

    for h in lst:
        lg = 0
        sm = 0
        for num in citations:
            if h <= num:
                lg += 1
        if lg >= h:
            answer = h
            break

    return answer


# 깔끔스한 풀이
def solution(citations):
    citations.sort()
    length = len(citations)

    for i in range(length):
        if citations[i] >= length - i:
            return length - i

    return 0