def combination(i, m, ii):
    if i == m:
        print(*result)
        return
    else:
        for j in range(ii, N+1):
            result[i] = j
            combination(i+1, m, j)
            result[i] = 0

N, M = map(int, input().split())
result = [0] * M
combination(0, M, 1)