N = int(input())

paper = [[-1]*1001 for _ in range(1001)]
for order in range(N):
    i1, j1, i2, j2 = map(int, input().split())
    for i in range(i1, i2+i1):
        for j in range(j1, j2+j1):
            paper[i][j] = order
result = [0]*N
for i in range(1001):
    for j in range(1001):
        if paper[i][j] >= 0:
            result[paper[i][j]] += 1
for i in range(N):
    print(result[i])