# 3에서 가까운 벽부터(1) 제거하고
# 제거해서 가는 중에 result보다 길면 짜르는 코드를 넣자

def find_distance(ci, cj):
    global result
    q = []
    visited[ci][cj] = 1
    q.append((ci, cj))
    while q:
        ci, cj = q.pop(0)
        # 가지치기
        if visited[ci][cj] >= result:
            break
        # 도착!
        if ci == N and cj == M:
            return visited[ci][cj]
        # 계속 탐색
        for dr in range(4):
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0<= ni <N and 0<= nj <M and arr[ni][nj] != 1 and not visited[ni][nj]:
                # 지금까지 얼마 거리 왔는지를 visited에 저장
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni, nj))
    return -1

di = [0,1,0,-1]
dj = [1,0,-1,0]
N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
si, sj = 0,0 # 시작 인덱스 초기화
visited = [[False for _ in range(M)] for _ in range(N)]
# result 초기화
result = 10*10

# 첫 번째 1을 발견하면 그거 0으로 바꾸고
# 두 번째 1을 찾으러 그 다음값부터 출발
# 그래서 두개의 벽 없애고 나면
# 미로 탐색
for i1 in range(N):
    for j1 in range(M):
        if arr[i1][j1] == 1:
            arr[i1][j1] = 0
            # visited 초기화 해주고 미로 탐색해야지^^
            visited = [[False for _ in range(M)] for _ in range(N)]
            tmp = find_distance(si,sj)
            if tmp >= 1 and result > tmp:
                result = tmp
            arr[i1][j1] = 1
# 결과 출력
if result == 10*10:
    print(-1)
else:
    print(result)