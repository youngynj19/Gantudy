'''
문제
방향성이 없는 그래프가 주어진다. 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
또한 세준이는 두 가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데,
그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 E가 주어진다. (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다. (1 ≤ c ≤ 1,000)
다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다. (v1 ≠ v2, v1 ≠ N, v2 ≠ 1)
임의의 두 정점 u와 v사이에는 간선이 최대 1개 존재한다.

출력
첫째 줄에 두 개의 정점을 지나는 최단 경로의 길이를 출력한다. 그러한 경로가 없을 때에는 -1을 출력한다.
'''

import sys
import heapq

def dij(s, e):
    # if e == must1:
    #     never1 = V
    # never1 = V if (e == must1 or e == must2) else -1
    # never2 =

    dis = [1000000000] * (V + 1)
    pq = []
    dis[s] = 0
    heapq.heappush(pq, (0, s))

    while len(pq) > 0:
        cur_fee, cur = heapq.heappop(pq)

        # if fee[cur] != d:
        #     continue

        for i in range(len(injub[cur])):
            # if injub[cur][i][1] != never:
            #     continue
            nxt_fee = cur_fee + injub[cur][i][0]
            nxt = injub[cur][i][1]
            if dis[nxt] > nxt_fee:
                dis[nxt] = nxt_fee
                heapq.heappush(pq, (nxt_fee, nxt))
    # print(dis)
    return dis[e]


V, E = map(int, sys.stdin.readline().split())
injub = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, d = map(int, sys.stdin.readline().split())
    injub[a].append((d, b))
    injub[b].append((d, a))

must1, must2 = map(int, sys.stdin.readline().split())

ans1 = dij(1, must1) + dij(must1, must2) + dij(must2, V)
ans2 = dij(1, must2) + dij(must2, must1) + dij(must1, V)

if min(ans1, ans2) >= 1000000000:
    print(-1)
else:
    print(min(ans1, ans2))

'''
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

7
'''