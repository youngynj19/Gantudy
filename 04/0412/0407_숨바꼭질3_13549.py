'''
문제
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력
수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

예제 입력 1
5 17
예제 출력 1
2
'''

from collections import deque

def short_cut(i):
    visited[i] = True
    dis[i] = 0
    # dis_index.append(i)
    # dis_index.append(0)
    # 초기값 채워주고(시작지점에서 갈 수 있는 곳 시간계산)
    for j in [i-1, i+1, i*2]:
        if not visited[j] and 0 <= j <= 100000:
            dis[j] = 0 if j == i*2 else 1
            # dis_index.append(j)
            # if j == i*2:
            #     dis_val.append(0)
            # else:
            #     dis_val.append(1)
    # 최단지점을 골라서 i가 점프점프 합니다!
    # 그래서 i == M이면 종료해도 됨!
    while i != M:
        # 다음 i를 정하기 위해
        # 시간이 가장짧게 걸리는애를 minn이랑 비교하면서 골라서
        # ni에 넣을꺼
        minn = 1000000
        ni = 0
        for j in range(100001):
            if not visited[j] and minn > dis[j]:
                minn = dis[j]
                ni = j
        # for j in range(len(dis_index)): # j는 dis리스트상의 인덱스(val과 index를 맞추어주는 용도)
        #     idx = dis_index[j] # 실제 장소 인덱스값
        #     if not visited[idx] and minn > dis_val[j]:
        #         minn = dis_val[j]
        #         ni = idx
        # visited 표시해줘서 밑에 for문에서 안걸리게!
        visited[ni] = True
        # j에서 갈 수 있는 노드를 파악
        # 거기까지 가는 최단시간 지금까지 계산해놓은 값 vs j에서 거기로 가는 최단시간
        for idx in [ni+1, ni-1, ni*2]:
            if not visited[idx] and 0<= idx <=100000:
                dis[idx] = min(dis[idx], dis[ni]) if idx == ni*2 else min(dis[idx], dis[ni]+1)

                #ㅠㅜㅠㅜㅜㅜㅠㅠㅠ
                # dis_index.append(idx)
                # if j == i * 2:
                #     dis_val.append(min(dis_val[idx], dis[ni]))
                # else:
                #     dis_index.append(1)



        # 이제 ni로 진짜 이동
        i = ni
        # print(dis)

N, M = map(int, input().split())
visited = [False for _ in range(1000000)]
dis = [1000000 for _ in range(1000000)]
# dis_index = deque()
# dis_val = deque()

short_cut(N)
print(dis[M])



# 순간이동이랑 걷는거랑 시간이 다름
# 즉 같은 레벨이라고 볼 수가 없고
# 많이 걷다가 순간이동 몇 번 해서 bfs를 통해 먼저 도착했다고 해서 얘가 최단시간이라는 보장은 x
# 순간이동만 냅다하다가 걷기 몇 번 만에 도착할 수도 있는데 그럴 떈 bfs레벨은 커도
# 시간은 짧을 수 있기 때문

# from collections import deque
#
# def bfs(i):
#     q = deque()
#     # 처음부터 만나면 0초 걸리는거니까
#     visited[i] = 0
#     q.append(i)
#     while q:
#         i = q.popleft()
#         # 현재 지점이 도착지점?! - visited에 표시한 시간 반환!
#         if i == M:
#             return visited[i]
#         # 세개에 대해 모두 돌려야하고
#         for ni in [i-1, i+1, i*2]:
#             # 범위안에 있으면서 방문한 적 없으면 q에 넣기
#             # if 0<= ni <=100000 and visited[ni] == -1:
#             if 0 <= ni <=200000 and visited[ni] == -1:
#                 # 순간이동은 시간증가ㄴㄴ, 걷기는 시간증가ㅇㅇ
#                 if ni == i * 2:
#                     visited[ni] = visited[i]
#                 else:
#                     visited[ni] = visited[i] + 1
#                 q.append(ni)
#
#
# N, M = map(int, input().split())
# # visited에 시간을 표시해줄 생각
# visited = [-1 for _ in range(200001)]
#
# print(bfs(N))