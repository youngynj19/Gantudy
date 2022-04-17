def combination(i, m):
    if i == m:
        print(*result)
        return
    else:
        for j in range(1, N+1):
            result[i] = j
            combination(i+1, m)
            result[i] = 0

N, M = map(int, input().split())
result = [0] * M
combination(0, M)