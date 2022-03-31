# 프로그래머스 [3차] 파일명 정렬

# for문을 이용
def solution(files):
    answer = []

    lst = []
    for idx, file in enumerate(files):
        s = n = rest = ''
        s_flag = True
        for i, each in enumerate(file):
            if each.isdigit():
                n += each
                s_flag = False
            elif s_flag:
                s += each.lower()
            else:
                rest = file[i:]
                break

        lst.append((s, n, idx))

    print(lst)
    lst.sort(key=lambda x: (x[0], int(x[1]), x[2]))

    for i in lst:
        answer.append(files[i[2]])

    return answer


# 정규표현식 이용
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(s) for s in sort]