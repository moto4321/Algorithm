# 세수의 합

###배열을 입력 받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하시오

nums = [-1,0,1,2,1,-1,-4]


def bruteforce(nums):
    result = []
    nums.sort()

    length = len(nums)
    for i in range(length - 2):
        if nums[i] > 0 or (i > 0 and nums[i] == nums[i-1]):
            continue
        for j in range(i + 1, length - 1):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            for k in range(j + 1, length):
                if k > j + 1 and nums[k] == nums[k-1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
    print(result)
    return result
bruteforce(nums)
#계산 시간은 O(n^3)으로 시간이 오래 걸림.. 쓸만한 방법이 아니다.




# [ A,    B ,  C,   D ,   E]
# (고정)  ><             (고정)
# (고정)       ><        (고정)
#             .....
#      (고정)  ><        (고정)
#      (고정)       ><   (고정)
# 어라 , 이것도 아닌데. ?





def threeSum(nums):
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복값제거
        if i > 0 and nums[i] == nums[i - 1]:
            continue

            # 간격 좁히기 / 0보다 작으면 왼쪽 증가 // 0보다 크면 오른쪽 증가
            #[ A,    B ,  C,   D ,   E]
            #(고정)  >>              <<
            #            >>         <<
            #             .....
            #      (고정)  >>        <<
            #      (고정)       >>   <<
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
                #찾게 되면 포인터 이동

    return result
#O(n^2)내로 해결 가능.!
