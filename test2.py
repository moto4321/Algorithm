inp = int(input())
box = 0
while True:
    if (inp % 5) == 0:
        box = box + (inp//5)
        print(box)
        break
    inp = inp - 3