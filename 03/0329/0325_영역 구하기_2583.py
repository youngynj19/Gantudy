'''
문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.



<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 
몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. 
M, N, K는 모두 100 이하의 자연수이다. 
둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 
오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 
모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 
입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.
'''

import sys
sys.stdin = open('1.txt')

def BFS(ci, cj):
    global area_cnt
    q = []
    # 넓이 1 추가
    area_cnt += 1
    # 방문 표시
    arr[ci][cj] = 1
    q.append((ci, cj))

    while q:
        ci, cj = q.pop(0)
        # 새 좌표 찾아서 조건에 맞으면
        # 넓이 추가, 방문표시, 큐에 append
        for dir in range(4):
            ni, nj = ci+di[dir], cj+dj[dir]
            if 0<= ni <N and 0<= nj <M and not arr[ni][nj]:
                area_cnt += 1
                arr[ni][nj] = 1
                q.append((ni, nj))

N, M, K = map(int, input().split()) # 세로, 가로, 사각형 갯수

# 0으로 초기화
arr = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    j1, i1, j2, i2 = map(int, input().split()) # 한 변 꼭지점 가로좌표, 꼭지점 세로좌표, 가로2, 세로2
    # 직사각형 1로 칠해주기
    for i in range(i1, i2):
        for j in range(j1, j2):
            arr[i][j] = 1

di ,dj = [0,1,0,-1], [1,0,-1,0]
cnt = 0 # 영역 갯수
area = [] # 각 영역 넓이
# 모든 영역 조회
for i in range(N):
    for j in range(M):
        # 현재 칸의 값이 0이면 cnt 추가 후 bfs순회
        if not arr[i][j]:
            cnt += 1
            area_cnt = 0 # 각 영역 넓이 1씩 더해줄 값
            BFS(i, j) # 좌표, 좌표
            # 함수에서 구한 영역 넓이 append
            area.append(area_cnt)

area = sorted(area)    
print(cnt)
print(*area)