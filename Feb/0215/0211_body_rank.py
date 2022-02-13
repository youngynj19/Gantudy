# 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨
# 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1

# a = [[],[],...,[]]
# a[0]에 대해 for문을 돌릴까요?...
# 아 for문이지만 이전꺼는 제외하게
# 1,2 다 크다 / 1같고 2 크다 / 1크고 2같다 / 1,2 다 같다 / 1크고 2작다 / 1작고 2크다
# 를 다 계산했찌만 다 헛짓거리


N = int(input())

students = []
for _ in range(N):
    students.append(list(map(int, input().split()))+[1])
# print(students)
# [[55, 185, 1], [58, 183, 1], [88, 186, 1], [60, 175, 1], [46, 155, 1]]

for i in range(N-1):
    for j in range(i, N):
        if students[j][0] == students[i][0] and students[j][1] == students[i][1]:
            pass
        elif students[j][0] >= students[i][0] and students[j][1] >= students[i][1]:
            students[i][2] += 1
        elif students[i][0] >= students[j][0] and students[i][1] >= students[j][1]:
            students[j][2] += 1

for i in range(N):
    print(students[i][2], end=' ')





# #백준 답

# N = int(input())

# students = []
# for _ in range(N):
#     students.append(list(map(int, input().split()))+[1])
# # print(students)
# # [[55, 185, 1], [58, 183, 1], [88, 186, 1], [60, 175, 1], [46, 155, 1]]

# for i in range(N-1):
#     for j in range(i, N):
#         if students[j][0] > students[i][0] and students[j][1] > students[i][1]:
#             students[i][2] += 1
#         elif students[i][0] > students[j][0] and students[i][1] > students[j][1]:
#             students[j][2] += 1

# for i in range(N):
#     print(students[i][2], end=' ')

