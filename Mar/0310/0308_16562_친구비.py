# 학생 i에게 Ai만큼의 돈을 주면 친구가 되어준다!
# 친구의 친구는 친구다
# 가장 적은 비용으로 모든 사람과 친구가 되는 방법

# 친구 찾을 때마다 해당 금액 찾아서 최소금액 저장 
# 끝나면 그걸 플러스 해나가기

import sys
# sys.stdin = open("2.txt")
sys.setrecursionlimit(100000)

def dfs(i):
    global min_fee
    visited[i] = True
    min_fee = min(min_fee, k_lst[i])

    for nxt in links[i]:
        if visited[nxt]:
            continue
        dfs(nxt)

N, M, k = map(int, sys.stdin.readline().rstrip().split())

k_lst = [0] # 친구비 리스트
# 친구비 받기(인덱스 1번 부터)
k_lst += list(map(int, input().split()))

# 친구 관계도 받기
links = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    links[a].append(b)
    links[b].append(a)

visited = [False for _ in range(N + 1)]

result = 0 # 모든 친구를 사귀려면 필요한 돈

# 모든 사람 순회하면서 함수 내에서 
for frd in range(1, N+1):
    min_fee = 10000
    if visited[frd]:
        continue
    # 함수 안에서 최소 금액을 계속 비교해나가면서 찾아가자
    # 리턴 없이 함수가 끝났을 때의 최소값을 그대로 더하게
    dfs(frd)
    result += min_fee

print(result) if k >= result else print('Oh no')