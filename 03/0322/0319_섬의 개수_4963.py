'''
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 
섬의 개수를 세는 프로그램을 작성하시오.

한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 
걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 
한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 
각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. 
w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
'''

import sys
# sys.stdin = open("1.txt")
sys.setrecursionlimit(10000000)

def dfs(i,j):
    di = [-1, -1, -1, 0, 1, 1, 1, 0]
    dj = [-1, 0, 1, 1, 1, 0, -1, -1]
    visited[i][j] = True

    for dir in range(8):
        ni, nj = i + di[dir], j + dj[dir]
        if ni in range(N) and nj in range(M):
            if arr[ni][nj] and not visited[ni][nj]:
                dfs(ni,nj)

# 언제 0,0이 나와서 탈출할 지 모르겠어서
while True:
    M, N = map(int, input().split())
    # 탈출조건
    if M == 0 and N == 0:
        break
    # 지도 받기
    arr = []
    for _ in range(N):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    visited = [[False for _ in range(M)] for _ in range(N)] # visited 리스트
    cnt = 0 # 출력값
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                cnt += 1
                dfs(i,j)
    print(cnt)