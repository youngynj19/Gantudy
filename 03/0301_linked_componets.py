def WFS(i):
    global cnt
    if visited[i] == 0:
        cnt += 1
        queue = []
        queue.append(i)
        while queue:
            i = queue.pop()
            if not visited[i]:
                visited[i] = True
                # print(visited)
                for w in range(1, N+1):
                    if arr[i][w] == 1 and visited[w] == 0:
                        queue.append(w)


N, M = map(int, input().split())
link = []
for _ in range(M):
    link.append(list(map(int, input().split())))

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    arr[link[i][0]][link[i][1]] = 1
    arr[link[i][1]][link[i][0]] = 1

cnt = 0
visited = [0] * (N+1)

for i in range(1, N+1):
    WFS(i)

print(cnt)





# N, M = map(int, input().split()) # 정점, 간선의 수
# '''
# 받을 때 마다 앞에 애들이랑 비교하면서 집합을 만들어나갈 생각
# 1,2 [[1, 2]]
# 3,4 [[1, 2], [3, 4]]
# 2,3 [[1, 2, 3, 4]]
# 5,6 [[1, 2, 3, 4], [5, 6]]
# '''
# link = [] # 연결 요소 리스트
# for _ in range(M):
#     new_link = list(map(int, input().split())) # 일단 간선 받고
#     i = [] # 이전 간선들 중 겹치는 애들 인덱스 번호
#     # 이전 간선들 중 겹치는 애들 인덱스 번호 받기
#     # 겹치는거 없으면 걍 새로운 set 추가
#     for j in range(len(link)):
#         if new_link[0] in link[j] or new_link[1] in link[j]:
#             i.append(j)
#             link[j] |= set(new_link)
#             # print("for done", end=' ')
#             # print(i)
#     # 겹치는 set이 두개면 두 개면 그 두개 합치기
#     if len(i) >= 2:
#         link[i[0]] |= link.pop(i[1])
#     elif len(i) == 0:
#         link.append(set(new_link))
#         # print('else done', end=' ')
#     # print(link)
# print(len(link))





# N, M = map(int, input().split())
# link = []
# # k = 0
# for _ in range(M):
#     link.append(list(map(int, input().split())))
#     # new_link = list(map(int, input().split()))
#     # if new_link[0] not in link and new_link[1] not in link:
#     #     k += 1
#     # link += new_link

# comp = [[0] for _ in range(N)]
# k = 0
# for i in range(M):
#     for j in range(k):
#         if link[i][0] in comp[j] or link[i][1] in comp[j]:
#             comp[j] += link[i]
#     else:
#         comp[k] += link[i]
#         k += 1
# print(comp)

# result = 0
# while comp[result] != [0]:
#     result += 1
    

# print(result)