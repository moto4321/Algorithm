# 1157
words = input().upper()
unique_words = list(set(words))

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt) # count 숫자를 리스트에 append