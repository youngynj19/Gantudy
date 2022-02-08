# 처음부터 나온 순서대로
# 먹는 것을 중단했다면, 그 이후에 나온 버섯은 모두 먹을 수 없다
# 점수의 합을 최대한 100에 가깝게

# 입력값 받을 리스트
mushroom_ls = []
for i in range(10):
    mushroom_ls.append(input())

mushrooms = 0
now_mush = 0
for mush in mushroom_ls:
    now_mush = int(mush) # 지금 있는 버섯 점수 : 나중에 필요함
    mushrooms += now_mush  # 모은 점수
    if mushrooms >= 100: # 종료조건 : 100점 넘기면
        break

last_mush = mushrooms - now_mush # 바로 전 점수 합
# 바로 전 점수합이랑 지금 점수합중 100이랑 더 가까운걸 출력
print(mushrooms) if mushrooms-100 <= 100-last_mush else print(last_mush)