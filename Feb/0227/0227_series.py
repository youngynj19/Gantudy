
N, K = map(int, input().split())
tempr = list(map(int, input().split()))

result = pre_tem = sum(tempr[:K])
for i in range(N-K):
    tem = pre_tem - tempr[i] + tempr[i+K]
    if tem > result:
        result = tem
    pre_tem = tem
print(result)