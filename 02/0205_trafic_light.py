# 도로에 진입했을 때, 모든 신호등의 색상은 빨간색이고, 사이클이 막 시작한 상태이다. 
# 상근이는 1초에 1미터를 움직인다.
# 도로의 끝까지 이동하는데 걸리는 시간?

N, L = map(int, input().split())

# 빨간색에서 다시 빨간불로 돌아오는 시간을 한 사이클
# 나머지가 어느 구간에 속하냐에따라 ㅇㅇㅇ

time = 0 # 흐르는 시간
distance = 0 # 이전 trafic sign 의 D... 지금 D에서 빼서 중간 거리만 계산
for i in range(N):
    D, R, G = map(int, input().split())
    time += D-distance # 현 위치에서 신호등까지 가는데 걸리는 시간
    # print("next trafic", time)
    if time % (R+G) < R: # 빨간불에 걸리면
        # 빨간불 남은 시간 :
        # 빨간불 총 시간 - 차가 도착했을 때 빨간분이 흐른 시간
        time += R - (time % (R+G))
        # print("time plue", R - (time % (R+G)))
        # 근데... 이게 0이 나옴.... 왤까요...
        # print("delay", time)
    L -= D-distance
    distance = D
time += L
print(time)