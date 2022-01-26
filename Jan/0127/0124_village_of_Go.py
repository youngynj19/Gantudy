# 야바위

order = input()

# yabawi = [1, 0, 0]
ball = 1 # ball에 걍 수를 대입

for chr in order: # 받은 문자열로 for문 돌리기
    if chr == 'A': # 각 알파벳에 따라 조건 나누기
        # yabawi[0], yabawi[1] = yabawi[1], yabawi[0]
        if ball == 1: # 각 ball 값에 따라 조건 둘씩 나누기
            ball = 2
        elif ball == 2:
            ball = 1
    elif chr == 'B':
        # yabawi[2], yabawi[1] = yabawi[1], yabawi[2]
        if ball == 3:
            ball = 2
        elif ball == 2:
            ball = 3
    else:
        # yabawi[0], yabawi[2] = yabawi[2], yabawi[0]
        if ball == 1:
            ball = 3
        elif ball == 3:
            ball = 1

print(ball)

# ball에 int 대임
# 단순 if절 중첩으로 풀음