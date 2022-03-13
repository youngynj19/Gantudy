# 학교에서 집으로 가는 경로에서 만나는 
# 숫자와 연산자의 연산 결과의 최댓값과 최솟값

def dfs(i, j, n, opr, cnt):
    global maximum
    global minimum
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

    

N = int(input()) # 지도 크기

# 지도 받기
arr = [[] for _ in range(N)]
for i in range(N):
    arr[i] = list(map(str, input().split()))

maximum = -5**6 # 최대값... 
# 0이 최대값 아닙니다..... 연산 문제에서 틀렸을 땐 초기값들 확인해보세요
minimum = 5**6 # 최소값
# cnt = 숫자일지 문자일지 결정해서 계산 유도하는 인덱스
# 초기화 때문에 '+' 넣어줌
dfs(0, 0, 0, '+', 0)

print(maximum, minimum)
















# def dfs(i, j, n, opr):
#     global maximum
#     global minimum
#     global cnt
#     global N
#     cnt += 1
#     print(f'cnt:{cnt}, val:{arr[i][j]}')
#     # 연산할 만큼 했다면
#     if cnt == N*2:
#         maximum = max(maximum, n)
#         minimum = min(minimum, n)
#         cnt -= 1
#         return
#     # 홀수일땐 숫자 받고 연산
#     if cnt%2:
#         if opr == '+':
#             n += int(arr[i][j])
#         elif opr == '-':
#             n -= int(arr[i][j])
#         else:
#             n *= int(arr[i][j])
#     # 짝수일 땐 연산자 새로 받기
#     else:
#         opr = arr[i][j]
#     # i+1 해보기
#     if i+1 < N:
#         dfs(i+1, j, n, opr)
#     if j+1 < N:
#         dfs(i, j+1, n, opr)
#     return

    

# N = int(input()) # 지도 크기

# # 지도 받기
# arr = [[] for _ in range(N)]
# for i in range(N):
#     arr[i] = list(map(str, input().split()))

# maximum = 0 # 최대값
# minimum = 5**6 # 최소값
# cnt = 0 # 숫자일지 문자일지 결정해서 계산 유도하는 인덱스
# # 초기화 때문에 '+' 넣어줌
# dfs(0, 0, 0, '+')

# print(maximum, minimum)