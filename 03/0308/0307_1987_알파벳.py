def dfs(i, j, n, opr, cnt):
    global N
    cnt += 1
    # print(f'cnt:{cnt}, val:{arr[i][j]}, n:{n}')
    # 홀수일땐 숫자 받고 연산
    if cnt%2:
        if opr == '+':
            n += int(arr[i][j])
        elif opr == '-':
            n -= int(arr[i][j])
        else:
            n *= int(arr[i][j])
    # 짝수일 땐 연산자 새로 받기
    else:
        opr = arr[i][j]
    # i+1 해보기
    if i+1 < N:
        dfs(i+1, j, n, opr, cnt)
    if j+1 < N:
        dfs(i, j+1, n, opr, cnt)
    # 연산할 만큼 했다면
    if cnt == N*2 - 1:
        if maximum < n:
            maximum = n
        if minimum > n:
            minimum = n
        return
    return