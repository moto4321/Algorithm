# 실패율

def solution(N, stages):
    failure = 0
    failure_list = []
    answer = []
    cnt = 0
    length = len(stages)

    for i in range(1, N + 1):
        cnt = 0
        if i in stages:
            cnt = stages.count(i)
            failure = cnt / length
            length -= cnt
        else:
            failure = 0

        # while i in stages:
        #     stages.remove(i)

        failure_list.append((failure, i))

    failure_list.sort(key=lambda x: (-x[0], x[1]))

    for k in failure_list:
        answer.append(k[1])

    return answer