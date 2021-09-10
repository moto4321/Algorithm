n = int(input())
arr = list(map(int, input().split()))

new = []

m = max(arr)
pt = 0

for i in range(len(arr)):
    scr = arr[i]/m*100
    new.append(scr)

for i in range(len(new)):
    pt += new[i]

print(pt/n)