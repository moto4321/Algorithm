# 5와 6의 차이
a, b = input().split()

max_a = ''
min_a = ''
max_b = ''
min_b = ''
for num in a:
    if num == '5' or num == '6':
        max_a += '6'
        min_a += '5'
    else:
        max_a += num
        min_a += num

for num in b:
    if num == '5' or num == '6':
        max_b += '6'
        min_b += '5'
    else:
        max_b += num
        min_b += num

print(int(min_a) + int(min_b), int(max_a) + int(max_b))


# 더 나은 풀이
a, b = input().split()
min_num = int(a.replace('6', '5')) + int(b.replace('6', '5'))
max_num = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(min_num, max_num)

