'''
문제
N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다.
이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다.
하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다.
N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

입력
첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다.
두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한 소요시간 Ti가 들어온다.
시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

출력
첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.

예제 입력 1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
예제 출력 1
10
'''

def fastest_time(s, e):
    visited[s] = True
    for nxt in range(1, N+1):
        time[nxt] = adjM[s][nxt]

    for _ in range(N):
        nxt = -1
        min_val = INF
        for i in range(1, N+1):
            if not visited[i] and min_val > time[i]:
                nxt = i
                min_val = time[i]
        visited[nxt] = True

        for i in range(1, N+1):
            if 0< adjM[nxt][i] <INF:
                time[i] = min(time[i], time[nxt]+adjM[nxt][i])
        print(time)
    return time[e]

N, M, X = map(int, input().split())

INF = 1000000
adjM = [[INF] * (N+1) for _ in range(N+1)]
for i in range(N+1):
    adjM[i][i] = 0

for i in range(M):
    s, e, val = map(int, input().split())
    adjM[s][e] = val
print(adjM)

# 각 마을에서 파티마을로 가는 최소시간, 오는 최소시간 계산해서 비교하기
maxx = -1
for i in range(1, N+1):
    tmp = 0
    time = [INF for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    # print(f'i{i} X{X}')
    tmp += fastest_time(i, X)
    # print(f'X{X} i{i}')
    tmp += fastest_time(X, i)
    # print(f'i{i} tmp{tmp}')
    if maxx < tmp:
        maxx = tmp

print(maxx)


# tree = [i for i in range(N+1)]
# adj = [[] for _ in range(M)]
# time = [0 for _ in range(N+1)]
#
# for i in range(M):
#     adj[i] = list(map(int, input().split()))
#
# adj.sort(key=lambda x : x[2])
# print(adj)
# # 이제 adj의 길들을 하나씩 연결해줄건데
# # 한 번 연결하고나서 1~N까지 X에 갈 수 있는지 or X에서 1~N까지 갈 수 있는지 체크
# # 갈 수 있을 때마다 time에 표시 (하고 flag(from 0)도 1씩 증가?)
# # time이 다 표시 되었으면 그 때 종료하고 (flag가 (N-1)*2가 되었을 때 종료하는 식으로?)
# # time에서 제일 큰 값 출력?