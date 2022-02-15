# 두 정수 사이에 있는 수의 합

# 대충 for문 돌리거나 sum 넣어버리면 시간초과;;
# 부호가 다른 경우는 더 빨리 계산하게!

# A, B중 뭐가 음수고 뭐가 절대값이 더 크고 그런거 다 조건으로 붙이기 귀찮아서 리스트로 받고 정렬!
numbers = list(map(int,input().split()))
numbers.sort()
A = numbers[0]
B = numbers[1]

# A,B 부호가 같은 경우
if A*B >= 0:
    print(sum(range(A,B+1)))
# -3 10
elif -A < B:
    # 4 10
    print(sum(range(-A+1,B+1)))
# -10 3
else:
    # -10 -4
    print(sum(range(A,-B)))




# A,B = map(int,input().split())
# summation = 0
# for i in range(A, B+1):
#     summation += i
# print(summation)


# A,B = map(int,input().split())
# print(sum(range(A,B+1)))