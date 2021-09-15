words = input().upper() # 문자열을 대문자로 만들어줌

cnt = words.count(x) # x의 개수를 카운트

# reverse reversed 차이
# reverse
list에만 적용됨
li = [1, 2, 3]
li_reverse = li.reverse()
print(li) # li자체를 바꿈

# reversed
li = [ i for i in range(5) ]
print(list(reversed(li)))  # [4,3,2,1,0]
print(li)  # [0,1,2,3,4]