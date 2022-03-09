'''
8
0 1 0 1 0 0 0 1
2
1 3
2 3
'''

# 남자는 걍 느낌 그대로 가주면 될 듯
def instruction_for_male(num):
    for i in range(1, N+1):
        if i % num == 0:
            switch[i] = 1 if switch[i] == 0 else 0
    # print(f'male : {switch}')

def instruction_for_female(num):
    # 비교해 줄 두 원소 초기화 해서 while들어갈 때 비교 할 수 있게
    # 그리고 while 안에서 업뎃
    i = 0 # num에서의 거리
    l, r = num - i, num + i # 대칭인 위치에 있는 left, right 두 값
    # 여자는 우선 num +- i가 범위 안벗어나는 내에서
    # 같다면 하나씩 수행해 나가는 식으로
    while 1 <= l and r <= N and switch[l] == switch[r]:
        if switch[r] == 0:
            switch[r] = switch[l] = 1
        elif switch[r] == 1:
            switch[r] = switch[l] = 0
        i += 1
        l, r = num - i, num + i
    # print(f'female : {switch}')


N = int(input()) # 스위치 수
# 스위치 실제 번호랑 인덱스번호 맞춰주려고 하나 더 잡음
# 인풋 받을 때도 슬라이싱으로 받고
switch = [-1] * (N+1)
switch[1:] = list(map(int, input().split())) # 스위치 상태
M = int(input()) # 학생 수
# student = [0] * M # 학생 상태 리스트
# for i in range(M): # 학생 상태 받아줌
#     student[i] = list(map(int, input().split()))

# 학생 한 명 받을 때마다 스위치 바꾸고 다음 학생 받을 생각
for _ in range(M):
    student = list(map(int, input().split())) # 학생 한 명씩 상태 받고
    if student[0] == 1:
        instruction_for_male(student[1])
    elif student[0] == 2:
        instruction_for_female(student[1])

i = 1
while i <= N:
    if i % 20 == 0:
        print(switch[i])
    else:
        print(switch[i], end=' ')
    i += 1