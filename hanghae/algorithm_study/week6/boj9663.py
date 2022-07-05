# N-Queen
n = int(input())

def back_tracking(rowPos):
    global answer
    if rowPos == n:
        answer += 1
        return
    
    for col in range(n):
        flag = True
        # 이전 행들에 대해서
        for row in range(rowPos):
            if queen_location[row] == col or rowPos - row == abs(col - queen_location[row]):
                flag = False
                break
        if flag:
            queen_location[rowPos] = col
            back_tracking(rowPos + 1)


answer = 0
queen_location = [0] * n
back_tracking(0)
print(answer)

# 또 다른 참고 풀이
n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(ans)
