# 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력

import sys
sys.stdin = open("1.txt")

def dfs_with_delta_search(i, j, N):
    ref = 1 # 집 들를 때 마다 하나씩 더해지는 친구
    # 왔다감 표시
    visited[i][j] = True
    # print(f'visited: {i, j, visited[i][j]}')

    di = [0, 1, 0, -1] # dirction list
    dj = [1, 0, -1, 0]

    for dir in range(4):
        ni = i + di[dir] # 새 좌표
        nj = j + dj[dir]
        # 조건1 : 새 좌표는 맵 안에 있어야 한다
        if 0 <= ni < N and 0 <= nj < N:
            # 조건2,3 : 1(집)이어야하며 방문한 적 없어야 한다
            if map_arr[ni][nj] == 1 and not visited[ni][nj]:
                # 집 한 채씩 더해
                ref += dfs_with_delta_search(ni, nj, N)
    # 집 한 채씩 더할 수 있게 반환값을 주는거지 + 다 센 집 채수도 반환하고
    return ref


N = int(input()) # 맵 크기

# 지도 받기
map_arr = [] 
for _ in range(N):
    map_arr.append(input())

visited = [[False for _ in range(N)] for _ in range(N)]

count = [] # 각 블럭 내 집 채수? 저장
# 각 지역 다 확인해볼 것 
for i in range(N):
    for j in range(N):
        # 해당 지역이 0(집이아님)이거나 이미 방문한 경우 바로 다음 지역 조회
        if map_arr[i][j] == 0 or visited[i][j] == True:
            continue
        # 조건에 맞는 집에서 탐색 시작
        # 해당 집이 포함된 블럭의 집의 채수 반환해서 저장
        count.append(dfs_with_delta_search(i, j, N))
        # print(f'house? {map_arr[i][j]}')
        # print(f'result: {dfs_with_delta_search(i, j, N)}')

sorted(count)
print(*count, sep='\n')

















# def WFS(i, j, count):
#     # global cnt
#     if visited[i][j] == 0:
#         # cnt += 1
#         queue = []
#         queue.append([i,j])
#         while queue:
#             i,j = queue.pop()
#             if visited[i][j] == '0':
#                 visited[i][j] = '1'
#                 count += 1
#                 di = [0,1,0,-1]
#                 dj = [1,0,-1,0]
#                 for dir in range(4):
#                     ni, nj = i + di[dir], j + dj[dir]
#                     # print(ni, nj)
#                     if map[ni][nj] == 1 and visited[ni][nj] == '0':
#                         queue.append([ni][nj])
#     return count


# N = int(input())

# # 0으로 감싸서 지도 만들기
# map = ['0'*(N+2)]
# for _ in range(N):
#     map.append('0' + input() + '0')
# map.append(['0'*(N+2)])
# # print(map)

# visited = ['0' * (N+2) for _ in range(N+2)]
# # print(visited)

# cnt = 0
# # print(visited[1][1])
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         # print(i, j, visited[i][j])
#         if visited[i][j] == 0:
#             cnt = WFS(i,j,1)

# # sorted(cnt)
# print(cnt)







# import sys
# sys.setrecursionlimit(100000)

# # import sys
# # sys.stdin = open('1.txt')

# N = int(input())

# # 0으로 감싸서 지도 만들기
# map = ['0'*(N+2)]
# for _ in range(N):
#     map.append('0' + input() + '0')
# map.append(['0'*(N+2)])

# def dfs(i, j):
#     # global count
#     # count += 1
#     map[i][j] = '0'

#     di = [0,1,0,-1]
#     dj = [1,0,-1,0]
#     for dir in range(4):
#         if map[i + di[dir]][j + dj[dir]] == '0':
#             continue

#         dfs(i + di[dir], j + dj[dir])

# count = 0
# # cnt = []
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         # count = 0
#         if map[i][j] == '0':
#             continue

#         count += 1
#         dfs(i,j)

# print(count)