# N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여
# , 제일 위에 있는 카드를 바닥에 버린다. 
# 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 버린 카드들을 순서대로 출력

N = list(range(int(input()), 0, -1))

# list를 만들어서
# 계속 돌아가면서(while)
# 빼자하나씩

while len(N) > 0:
    print(N.pop(), end=' ')
    if len(N) == 0:
        break
    N.insert(0, N[-1])
    N.pop()
    