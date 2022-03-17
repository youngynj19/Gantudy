# 기본적인 BFS 코드
def BFS(i):
    global cnt
    visited = [0] * (N+1)
    queue = []
    queue.append(i)
    while queue:
        i = queue.pop()
        if not visited[i]:
            visited[i] = True
            # visit 하는 순간 cnt 추가
            cnt += 1
            for w in range(1, N+1):
                if connect[i][w] == 1 and not visited[w]:
                    queue.append(w)


N = int(input())
M = int(input())

connect = [[0 for _ in range(N+1)] for _ in range(N+1)] # 이차원 연결리스트
# 받자마자 이차원 연결리스트에 추가
for _ in range(M):
    dot1, dot2 = map(int, input().split())
    connect[dot1][dot2] = 1
    connect[dot2][dot1] = 1

cnt = 0
BFS(1)
# 1번 간 건 빼야해서 하나 빼서 출력
print(cnt-1)