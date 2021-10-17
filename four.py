# 선택정렬
li = [1, 5, 3, 7, 4, 9]

for i in range(len(li)):
    min_index = i
    for j in range(i + 1, len(li)):
        if li[min_index] > li[j]:
            min_index = j
    li[min_index], li[i] = li[i], li[min_index]

print(li)



# 삽입정렬
