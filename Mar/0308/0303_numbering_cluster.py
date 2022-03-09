# # 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력


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







import sys
sys.setrecursionlimit(100000)

# import sys
# sys.stdin = open('1.txt')

N = int(input())

# 0으로 감싸서 지도 만들기
map = ['0'*(N+2)]
for _ in range(N):
    map.append('0' + input() + '0')
map.append(['0'*(N+2)])

def dfs(i, j):
    # global count
    # count += 1
    map[i][j] = '0'

    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    for dir in range(4):
        if map[i + di[dir]][j + dj[dir]] == '0':
            continue

        dfs(i + di[dir], j + dj[dir])

count = 0
# cnt = []
for i in range(1, N+1):
    for j in range(1, N+1):
        # count = 0
        if map[i][j] == '0':
            continue

        count += 1
        dfs(i,j)

print(count)