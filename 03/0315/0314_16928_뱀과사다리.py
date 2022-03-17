import sys
from collections import deque

# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = 1

    while queue:

        target = queue.popleft()

        # 주사위 눈만큼 반복한다.
        for i in range(1, 7):
            dice = target + i

            # 100칸이 넘어가면 넘긴다.
            if dice > 100:
                continue

            cnt = graph[dice]

            # 탐색하지 않은 칸이라면 탐색한다.
            if visited[cnt] == 0:
                queue.append(cnt)
                visited[cnt] = visited[target] + 1

                # 100번째 칸까지 탐색했다면 리턴
                if cnt == 100:
                    return


n, m = map(int, sys.stdin.readline().split())

# 보드판을 표현, 사다리나 뱀인 경우에는 이동 후 좌표로 표시
graph = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] = b
    # [1,2,3,17,5,6,7,8]

# 탐색한 칸까지 가기 위한 주사위 던진 횟수를 체크
visited = [0] * 101

# 1번 칸부터 bfs 탐색
bfs(1)

# 100번째 칸까지 가기 위한 주사위 던진 횟수에서
# 1번 칸에서 카운트한 주사위 던진 횟수를 빼준다.
print(visited[100] - 1)









# def qsort(arr1, arr2, begin, end):
#     if begin < end :
#         p = partition(arr1, arr2, begin, end)
#         qsort(arr1, arr2, begin, p-1)
#         qsort(arr1, arr2, p+1, end)

# def partition (arr1, arr2, begin, end) :
#     pivot = (begin + end) // 2
#     L = begin
#     R = end
#     while L < R :
#         while(L<R and arr1[L]< a[pivot]) : L += 1
#         while(L<R and arr1[R]>=a[pivot]) : R -= 1
#         if L < R :
#             if L==pivot : pivot = R
#             arr1[L], arr1[R] = arr1[R], arr1[L]
#     a[pivot], a[R] = a[R], a[pivot]
#     return R    

# L, S = map(int, input().split())

# ladder1, ladder2 = [], []
# snake1, snake2 = [], []
# for _ in range(L):
#     a, b = map(int, input().split())
#     ladder1.append(a)
#     ladder2.append(b)
# for _ in range(S):
#     a, b = map(int, input().split())
#     snake1.append(a)
#     snake2.append(b)

# qsort(ladder1, ladder2 0, L-1)
# qsort(snake1, snake2, 0, S-1)