def qu(r, n):
    global cnt
    if r == n:
        cnt += 1

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
for _ in range(Q):
    cnt = 0
    print(qu(R, int(input())))