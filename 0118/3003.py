sets = list(map(int, input().split())) # 입력
sets_comp = [1, 1, 2, 2, 2, 8] # 원래 있어야하는 체스 말 갯수

# 두 리스트 비교
for i in range(6):
    print(sets_comp[i] - sets[i], end=(' '))