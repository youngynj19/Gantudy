def combination(i, m, ii): # 몇 개 넣었는지, 몇개까지 넣을 수 있는지, 어디부터가 후보군인지
    # 다 골랐으면 함 보여주고
    if i == m:
        print(*result)
        return
    else:
        for j in range(ii, N+1):
            if not used[j]:
                used[j] = True
                result[i] = j
                combination(i+1, m, j+1)
                result[i] = 0
                used[j] = False

N, M = map(int, input().split())
used = [False] * (N+1)
result = [0] * M
combination(0, M, 1)