N, M, L = map(int, input().split())

result = 0
counts = [0]*N # 각 친구 공 받은 횟수 리스트
counts[0] = 1 # 0번 친구 초기값
i = 0 # 공 받은 친구 초기값
while M not in counts:
    # 공 받은 친구가 홀수면
    if counts[i] % 2:
        '''
           ㅁ ㅁ
         ㅁ     ㅁ[0]
           ㅁ ㅁ
          [-2 = 4]
        '''
        # 시계방향을 리스트에 거스르는걸로 계산
        i = (i-L) % N # -2%6 = 4%6 = 4라고 함....
        counts[i] += 1
    else:
        i = (i+L) % N
        counts[i] += 1
    result += 1

print(result)
