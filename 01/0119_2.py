N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in A: # A에 들어있는 값 중
    if i < X: # X보다 작은 값이 있으면
        print(i, end=' ') # 출력하라