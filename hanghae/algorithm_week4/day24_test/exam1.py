# 프로그래머스 입국심사

def solution(n, times):
    answer = 0

    lo = 1
    hi = max(times) * n
    while lo <= hi:
        mid = (lo + hi) // 2
        total = 0
        for t in times:
            total += mid // t

        if total >= n:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return answer