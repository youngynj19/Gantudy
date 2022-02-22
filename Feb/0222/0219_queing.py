N = int(input())
lotto = list(map(int, input().split()))
order = [i for i in range(1, N+1)]
# print(order)

for i in range(N):
    for j in range(lotto[i]):
        # k는 i에서 lotto에 적힌 값 만큼 1씩 감소
        k = i-j
        order[k], order[k-1] = order[k-1], order[k]
for i in range(N):
    print(order[i], end=' ')