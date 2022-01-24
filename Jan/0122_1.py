N = int(input())
result = 1 # 곱할꺼니까 1로 초기화
for i in range(1,N+1): # 1부터 N까지
    result *= i
print(result)