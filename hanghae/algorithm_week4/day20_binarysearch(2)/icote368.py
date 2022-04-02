def fixed_point(lst):
    lo = 0
    hi = len(lst)

    # 결과값 lo 는, i < lo 인 모든 i 에 대하여 lst[i] < i
    while lo < hi:
        mid = (lo + hi) // 2
        if lst[mid] < mid:
            lo = mid + 1
        else:
            hi = mid  # mid - 1이 아닌 이유는 맨 처음 hi를 배열의 길이로 잡았기 때문.

    # 범위를 벗어나거나, 없는 경우.
    # lo 는 0에서부터 출발하므로, lo < 0 인 것은 검사하지 않아도 됩니다.
    if lo >= len(lst) or lo != lst[lo]:
        return -1
    return lo


assert fixed_point([-1, 1, 3, 5, 7]) == 1
assert fixed_point([-15, -6, 1, 3, 7]) == 3
assert fixed_point([-15, -4, 2, 8, 9, 13, 15]) == 2
assert fixed_point([-15, -4, 3, 8, 9, 13, 15]) == -1
assert fixed_point([-15, -6, 1, 2, 5]) == -1
assert fixed_point([-15, -6, -5, -4, -3]) == -1
assert fixed_point([3, 4, 5, 6, 7]) == -1