# 개미는 오른쪽 위 45도 방향으로 일정한 속력으로 움직이기 시작
# 경계면에 부딪치면 같은 속력으로 반사되어 움직
# t시간 후의 위치 (x,y)를 계산하여 출력


def ant_moving_in_rectangle(i, j, di, dj, w, h, T):
    rT = 0

    while 0 < i < w and 0 < j < h and rT<T:
        i += di
        j += dj
        rT += 1
    if (i == 0 or i == w) and not (j == 0 or j == h):
        # i의 한계점에 와있으면 di가 반대로 돌려진 채 while을 벗어났을 것
        # 그럼 j만 반대로 돌려주면 되겠네
        di = -di
    elif not (i == 0 or i == w) and (j == 0 or j == h):
        dj = -dj
    else:
        di, dj = -di, -dj
    print(f'i,j: {i, j}, di,dj: {di, dj}, rT: {rT}')
    while rT < T:
        in_line = (0 <= i <= w-h) if di > 0 else (h <= i <= w)
        # 긴 축에 속했으면
        if 0 == j or j == h:
            if in_line:
                i += di*h
                j += dj*h
                rT += h
                di = -di
                dj = -dj if j == 0 or j == h else dj
            else:
                if di > 0:
                    i += di * (w-i)
                    j += dj * (w-i)
                    rT += w-i
                    di = -di
                else:
                    i += di*i
                    j += dj*i
                    rT += i
                    di = -di
        else:
            if dj > 0:
                i += di * (h-j)
                j += dj * (h-j)
                rT += h-j
                dj = -dj
            else:
                i += di * j
                j += dj * j
                rT += j
                dj = -dj
        print(f'i,j: {i, j}, di,dj: {di, dj}, rT: {rT}')
    if (i == 0 or i == w) and not (j == 0 or j == h):
        # i의 한계점에 와있으면 di가 반대로 돌려진 채 while을 벗어났을 것
        # 그럼 j만 반대로 돌려주면 되겠네
        dj = -dj
        # 반대로 감
        i += di * (rT-T)
        j += dj * (rT-T)
    elif not (i == 0 or i == w) and (j == 0 or j == h):
        di = -di
        i += di * (rT-T)
        j += dj * (rT-T)
    else:
        i += di * (rT-T)
        j += dj * (rT-T)    




# 좌표 표기 특성상 w가 앞에와서 w = i좌표, h = j좌표로 볼꺼임
w, h = map(int, input().split()) # 방바닥 크기
i, j = map(int, input().split()) # 현재 개미 위치
T = int(input()) # 시간 제한
# 격자의 꼭지점을 리스트 한 공간으로 잡을 생각
# 0부터 h까지 있는 리스트가 0부터 w까지 늘어있는 꼴
# 즉 가로세로 각각 h+1, w+1개 있음
# arr = [[None]*(h+1) for _ in range(w+1)]
'''방바닥 array는 만들 필요 없음. 어짜피 w, h와 값 비교하는게 다라서ㅇㅇ'''

# 좌표계를 변환하면 이게 원래 좌표에서 우상향 맞음
di, dj = 1, 1 # 초기 방향
rT = 0 # 흐른 시간
# 빨리 계산하게 한 번씩 이동 안하고 할 만큼 다 이동할 생각
# 그래서 어쩔수없이
# 시간을 한 번은 초과할 수도 있고 그 후에 while 빠져나오게 설게

if w>h:
    di, dj = 1, 1 # 초기 방향
    ant_moving_in_rectangle(i, j, di, dj, w, h, T)
elif h>w:
    i, j = j, i # 긴거가 무조건 i좌표가 되게 할려고
    di, dj = -1, 1
    ant_moving_in_rectangle(i, j, di, dj, h, w, T)
    i, j = j, i
else:
    ant_moving_in_square(i, j, )



print(i, j)








# # 좌표 표기 특성상 w가 앞에와서 w = i좌표, h = j좌표로 볼꺼임
# w, h = map(int, input().split()) # 방바닥 크기
# i, j = map(int, input().split()) # 현재 개미 위치
# T = int(input()) # 시간 제한
# # 격자의 꼭지점을 리스트 한 공간으로 잡을 생각
# # 0부터 h까지 있는 리스트가 0부터 w까지 늘어있는 꼴
# # 즉 가로세로 각각 h+1, w+1개 있음
# # arr = [[None]*(h+1) for _ in range(w+1)]
# '''방바닥 array는 만들 필요 없음. 어짜피 w, h와 값 비교하는게 다라서ㅇㅇ'''

# # 좌표계를 변환하면 이게 원래 좌표에서 우상향 맞음
# di, dj = 1, 1 # 초기 방향
# rT = 0 # 흐른 시간
# # 빨리 계산하게 한 번씩 이동 안하고 할 만큼 다 이동할 생각
# # 그래서 어쩔수없이
# # 시간을 한 번은 초과할 수도 있고 그 후에 while 빠져나오게 설게
# while rT < T:
#     '''
#       0  j  2  3  h
#     0[ ][ ][ ][ ][ ]
#     i[ ][*][ ][ ][ ]
#     2[ ][ ][ ][ ][ ]
#     w[ ][ ][ ][ ][ ]
#     *이 있는 위치(1,1)에서
#     di = -1, dj = 1 우상방향일 때
#     i 방향으로는 i만큼 갈 수 있음
#     j 방향으로는 h-j만큼 갈 수 있음
#     '''
#     imax = i if di == -1 else w-i
#     jmax = j if dj == -1 else h-j

#     if imax > jmax:
#         # 더 적게 가는 만큼만 가야 범위 안벗어남
#         i += di * jmax
#         j += dj * jmax
#         # j방향이 짧다는거니까 j의 한계에 도달한거
#         # j방향 바꿔서 진행해야한단거
#         dj = -dj
#         # 시간 이만큼 흐름
#         rT += jmax
#     elif imax < jmax:
#         i += di * imax
#         j += dj * imax
#         di = -di
#         rT += imax
#     else:
#         # imax == jmax일 때
#         i += di * imax
#         j += dj * jmax
#         di, dj = -di, -dj
#         rT += imax

# # 초과한 시간만큼 반대로 가기
# if (i == 0 or i == w) and not (j == 0 or j == h):
#     # i의 한계점에 와있으면 di가 반대로 돌려진 채 while을 벗어났을 것
#     # 그럼 j만 반대로 돌려주면 되겠네
#     dj = -dj
#     # 반대로 감
#     i += di * (rT-T)
#     j += dj * (rT-T)
# elif not (i == 0 or i == w) and (j == 0 or j == h):
#     di = -di
#     i += di * (rT-T)
#     j += dj * (rT-T)
# else:
#     i += di * (rT-T)
#     j += dj * (rT-T)

# print(i, j)


'''
시간 초과 떠서 한 번씩 이동 안하고 할 만큼 다 이동할 생각
di, dj = 1, 1 # 초기 방향
# T번 수행 한 후 빠져나옴
# 처음 수행할 때부터 i, j가 바뀐 후 다음으로 넘어감
# 즉 빠져나왔을 땐 T번 움직인 뒤의 i, j값 저장되어있음 
for t in range(T):
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