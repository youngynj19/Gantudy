N = int(input())

paper = [[0]*100 for _ in range(100)]
for _ in range(N):
    i, j = map(int, input().split())
    for ii in range(i, i+10):
        for jj in range(j, j+10):
            paper[ii][jj] = 1
result = 0
for i in range(100):
    result += sum(paper[i])
print(result)