# a = [[],[],...,[]]
# a[0]에 대해 for문을 돌릴까요?...
# 아 for문이지만 이전꺼는 제외하게
# 1,2 다 크다 / 1같고 2 크다 / 1크고 2같다 / 1,2 다 같다 / 1크고 2작다 / 1작고 2크다 / 


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


# 2 2 1 2 5







# N = int(input())

# students = []
# for _ in range(N):
#     students.append(list(map(int, input().split()))+[1])
# # print(students)
# # [[55, 185, 1], [58, 183, 1], [88, 186, 1], [60, 175, 1], [46, 155, 1]]

# for i in range(N):
#     for j in range(N):
#         if i==j:
#             continue
#         if students[j][0] == students[i][0] and students[j][1] == students[i][1]:
#             pass
#         elif students[j][0] >= students[i][0] and students[j][1] >= students[i][1]:
#             students[i][2] += 1

# for i in range(N):
#     print(students[i][2], end=' ')