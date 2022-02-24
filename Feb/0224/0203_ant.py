# 개미는 오른쪽 위 45도 방향으로 일정한 속력으로 움직이기 시작
# 경계면에 부딪치면 같은 속력으로 반사되어 움직
# t시간 후의 위치 (x,y)를 계산하여 출력

w, h = map(int, input().split()) # 방바닥 크기
i, j = map(int, input().split()) # 현재 개미 위치
time = int(input()) # 흐른 시간
# 격자의 꼭지점을 리스트 한 공간으로 잡을 생각
# 0부터 h까지 있는 리스트가 0부터 w까지 늘어있는 꼴
# 즉 가로세로 각각 h+1, w+1개 있음
# arr = [[None]*(h+1) for _ in range(w+1)]
'''방바닥 array는 만들 필요 없음. 어짜피 w, h와 값 비교하는게 다라서ㅇㅇ'''

di, dj = 1, 1

'''
시간 초과 떠서 한 번씩 이동 안하고 할 만큼 다 이동할 생각
di, dj = 1, 1 # 초기 방향
# time번 수행 한 후 빠져나옴
# 처음 수행할 때부터 i, j가 바뀐 후 다음으로 넘어감
# 즉 빠져나왔을 땐 time번 움직인 뒤의 i, j값 저장되어있음 
for t in range(time):
    # 똑같은 방향으로 일단 움직여보기
    i += di
    j += dj
    i_in = 0 <= i <= w # i가 범위내에 있으면 True
    j_in = 0 <= j <= h # 이하동문
    # 움직일 수 있었는지 체크해주고 아니면 방향 바꾸고, 
    # 원래 움직였어야하는 곳까지 이동
    if not i_in and not j_in:
        # 코너에 걸렸을 땐 i, j방향 둘 다 반대로
        di, dj = -di, -dj
        i += 2*di
        j += 2*dj
    elif i_in and not j_in:
        # j에 걸린거면 j방향만 바꿔주면 됨
        dj = -dj
        j += 2*dj
    elif not i_in and j_in:
        # 이하 동문
        di = -di
        i += 2*di
print(i, j)
'''