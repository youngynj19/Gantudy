def BFS(i):
    # global cnt
    # if visited[i] == 0:
        # cnt += 1
    queue = []
    queue.append(i)
    cnt = 0
    visited[i] = cnt
    while queue:
        i = queue.pop()
        if i == b:
            return visited[i]
        # if visited[i] == 0:
            # visited[i] = cnt
            # print(visited)
        for w in range(1, N+1):
            if arr[i][w] == 1 and visited[w] == -1:
                visited[w] = visited[i]+1
                queue.append(w)
    return -1



N = int(input())
a, b = map(int, input().split())
M = int(input())

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    c, d = map(int, input().split())
    arr[c][d] = 1
    arr[d][c] = 1

# cnt = 0
visited = [-1] * (N+1)

# for i in range(1, N+1):
    # WFS(i)

print(BFS(a))

# print(cnt)