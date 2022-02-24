# 시계방향으로 돌아가면서 비어있는 좌석에 관객을 순서대로 배정한다
# 대기 순서가 K인 관객에게 배정될 좌석 번호 (x,y)를 찾는 프로그램

C, R = map(int, input().split()) # 극장 크기
K = int(input())
arr = [[0]*R for _ in range(C)] # 극장 array
'''
가로R
ㅁㅁ...ㅁㅁ 세로C
...         
ㅁㅁ...ㅁㅁ
'''

# 델타탐색을 이용해서 K번째에서의 현재 위치를 뽑아내자!
i, j = 0, 0 # 현재 위치
idx = 1 # 관람객 번호
# 초기화
arr[i][j] = idx
flag = R*C
# K번째일 때 while문 안에서 해당 관객의 좌석번호를 찾아서 빠져나올예쩡
# 혹시 K가 다다르기 전에 이미 자리가 꽉차도 빠져나오셈
while idx < K and idx < flag :
    # flag = 0 # K번째 관객이 들어갈 자리가 있는지 체크
    # 우 하 좌 상 순으로 바뀌긴 할껀데 while문이 끝날 때까진 방향 유지
    for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
        # 범위를 벗어나지 않고 아직 K번째 관객에 도착하지도 않았다면 while문 계속
        # 위치랑 관객 업뎃해주고 해당 좌석에 관객 앉혀주기
        while 0 <= i+di < C and 0 <= j+dj <R and arr[i+di][j+dj] == 0 and idx < K:
            i += di
            j += dj
            idx += 1
            arr[i][j] = idx
            # 이번 for문에서 한 번은 적어도 움직였습니다 체크
            # flag += 1
        # 혹시 K번째 관객에 걸려서 while을 빠져나온거면 for문 더 돌지말고
        # while 조건에도 걸릴테니 빠져나가셈 
        if idx == K:
            break
    
    '''
    이거는 90%쯤에서 오류뜸...

    # for문에 들어가서 한 번이라도 움직였다면(K가 착석했다면)
    # print(idx, i, j)
    # if idx == K and flag > 0:
        # print(i+1, j+1)
    # for문에서 한 번도 못 움직인채 빠져나온 경우, K는 빠이
    # elif flag == 0:
        # print(0)
        # break    
    '''
# K에 도달했으면 출력, 아니면 오류
if idx == K:
    print(i+1, j+1)
else:
    print(0)
