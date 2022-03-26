# 전화번호 목록


t = int(input())

for _ in range(t):
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())

    min_list = []

    length = 10001
    for num in lst:
        length = min(len(num), length)

    print(length)

    for num in lst:
        if len(num) == length:
            min_list.append(num)
            lst.remove(num)

    print(lst)
    print(min_list)

    for num in lst:
        if num[0:length] in min_list:
            print('NO')
            break
    else:
        print('YES')


# 정답 풀이
t = int(input())

for _ in range(t):
    n = int(input())
    phonebook = []

    for _ in range(n):
        phonebook.append(input())

    phonebook.sort(key=str)

    flag = True

    for i in range(len(phonebook) - 1):
        if phonebook[i] == phonebook[i + 1][:len(phonebook[i])]:
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')


