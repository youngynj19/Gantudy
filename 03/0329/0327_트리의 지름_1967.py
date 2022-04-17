import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]

def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        # 아직 방문 안했으면
        # 지금껏 거리에 현재 거리도 더해서 담아주고ㅇㅇ
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드걸리는 거리를 각각 표시
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
# 우선 1에서 가장 먼 노드의 번호 받고
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
# 해당 번호에서 다시 거리를 표시
dfs(start, 0)

print(max(distance))