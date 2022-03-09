# 사칙연산 문제와 답이 주어졌을 때,
# 이를 채점하는 프로그램을 작성하시오.

# C = int(input()) # 테스트 케이스 개수
# in_ls = []
# # in_ls, out_ls = [], [] # 인풋, 아웃풋 리스트

# for i in range(C): # 각 케이스에 따라
#     # temp = list(map(int, input().split()))
#     # in_ls += [temp]
#     in_ls.append(input()) # 각 케이스 테스트 받기
#     print(in_ls)

# count = 0
# while count < len(in_ls):
#     count += 1
#     x = int(in_ls[0])
#     y = int(in_ls[4])

#     if in_ls[2] == "+":
#         ans = x + y
#     elif in_ls[2] == "-":
#         ans = x - y
#     elif in_ls[2] == "*":
#         ans = x * y
#     else:
#         ans = x // y

#     print("correct") if ans == int(in_ls[8]) else print("False")

# 너무 길대요ㅠㅜㅠㅠㅠㅜ

C = int(input()) # 테스트 케이스 개수
in_ls = []
# in_ls, out_ls = [], [] # 인풋, 아웃풋 리스트

for i in range(C): # 각 케이스에 따라
    # temp = list(map(int, input().split()))
    # in_ls += [temp]
    in_ls.append(input()) # 각 케이스 테스트 받기
    # print(in_ls)

for count in range(C):
    x = int(in_ls[count][0])
    y = int(in_ls[count][4])

    if in_ls[count][2] == "+":
        ans = x + y
    elif in_ls[count][2] == "-":
        ans = x - y
    elif in_ls[count][2] == "*":
        ans = x * y
    else:
        ans = x // y

    print("correct") if ans == int(in_ls[count][8]) else print("False")

