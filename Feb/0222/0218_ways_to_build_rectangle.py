N = int(input())

# 회전은 해당 안됨 - 세로가 가로보다 긴건 ㄴㄴ
# 가로는 쭉쭉 늘어나도 세로로는 제곱이 될 때부터 늘어나게
# 그 조건 내의 정수에 관해서 나누어 떨어지면 사각형 만들어짐

result = 0 # 조건에 맞을 때마다 사각형 가능 경우 하나 추가
square = 2 # 2의 제곱일 때부터 생각하면 되니까 

for i in range(1, N+1):
    if i == square**2:
        square += 1
    # 2^2이 되기 전까진 range(1,2) 즉 1만, 
    # 4부터 (1,3) 즉 1~2 계싼
    for j in range(1, square):
        if i % j == 0:
            # rec[i] += 1
            result += 1
print(result)
'''
1
1
1
2
1
2
1
2
제곱일 땐 해당 제곱만큼 들어가게
'''