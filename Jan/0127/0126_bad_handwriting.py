# 숫자 ‘0’, ‘6’, ‘9’를 학생들의 기쁨을 위해 ‘9’로 통일시켜 버리기로 하였다.
# 학생들의 평균 성적과 가장 가까운 정수를 출력
# 그런 정수가 여러 개라면 그 중 가장 큰 것을 출력한다.

# 점수들 하나씩 받으면서 더하자

N = int(input())

result = 0
for i in range(N):
    n = input()
    if int(n.replace('6','9').replace('0','9')) <= 100: # 6, 0을 다 9로 변환 후 int로 바꾸기
        # 그런데 해당 값이 100보다 크면 그냥 본인 값 그대로 넣어야하니까 else 처리
        result += int(n.replace('6','9').replace('0','9'))
    else:
        result += int(n)

if result/N % 1 >= 0.5: # round가 안먹혀서 1로 나눈 나머지가 0.5 이상인 조건문으로 나눔
    print(result//N+1)
else:
    print(result//N)