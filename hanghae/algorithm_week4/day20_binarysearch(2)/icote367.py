def count_number(lst, target):
    left_idx = bisect.bisect_left(lst, target)
    if not (0 <= left_idx < len(lst) and lst[left_idx] == target):
        return -1

    right_idx = bisect.bisect_right(lst, target)
    return right_idx - left_idx


assert count_number(lst=[1, 1, 2, 2, 2, 2, 3], target=2) == 4
assert count_number(lst=[1, 1, 2, 2, 2, 2, 3], target=4) == -1