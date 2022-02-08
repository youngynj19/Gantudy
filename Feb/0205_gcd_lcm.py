# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# A, B = map(int, input().split())

# A_list, B_list = [], [] # 일단 A, B 모든 약수 모아놓을 리스트

# for i in range(1,A+1): # A의 약수면 리스트에 넣기
#     if not A%i:
#         A_list += [i]

# for i in range(1,B+1):
#     if not B%i:
#         B_list += [i]
# print(A_list) # 답 안나와서 일단 프린트라도 해봄
# print(B_list) # 근데 해보니까 set으로 묶으면 될 것 같길래 일단 해봄

# A_and_B = set(A_list) & set(B_list) # 해보니까 공약수들만 딱 모이길래 최대값 구함

# print(max(A_and_B))
# # print(A_or_B)

# AB_list = [] # A*B의 모든 약수 # 공배수는 저 방식으로 안풀려서 거시적으로 봄
# for i in range(1,A*B+1): # A*B의 약수면 리스트에 넣고
#     if not (A*B)%i:
#         AB_list += [i]

# AB_bigger = [] # A와 B의 공배수 * 공배수를 구하는 쪽으로
# for num in AB_list:
#     if not (num%A or num%B): # 둘 중 하나라도 1이면 괄호가 1 -> 0
#         AB_bigger += [num]
# print(min(AB_bigger))

# ########### set에서 제일 큰 애가 최대 공약수인가????? 맞음 밑에서 확인

# # a^3, b^3, c^3
# # a^2, b^5, d^1

# # 최대공약수
# # a^2, b^3

# # 최소공배수
# # = a^3, b^5, c^3, d^1
# # A*B = a^5, b^8, c^3, d^1
# # 의 모든 약수중에서
# # A와 B의 배수중 가장 작은 값




# A, B = map(int, input().split())

# AB_list = [] 
# for i in range(1,A*B+1):
#     if not (A*B)%i:
#         AB_list += [i]

# AB_smaller = []
# for num in AB_list:
#     if not (A%num or B%num):
#         AB_smaller += [num]
# print(max(AB_smaller))

# AB_bigger = [] 
# for num in AB_list:
#     if not (num%A or num%B):
#         AB_bigger += [num]
# print(min(AB_bigger))






# A, B = map(int, input().split())

# AB_smaller = []
# AB_bigger = [] 
 
# for i in range(1,A*B+1):
#     if not (A%i or B%i):
#         AB_smaller += [i]
#     elif not (i%A or i%B):
#         AB_bigger += [i]
        
# print(max(AB_smaller))
# print(min(AB_bigger))







A, B = map(int, input().split())

smallest = 0
biggest = 0 
 
for i in range(1,A*B+1): # 공배수, 공약수 다 나오는 리스트
    if not (A%i or B%i): # 에서 리스트도 빼고 공약수들만 골라내서 제일 마지막에 잡히는 애 넣음
        smallest = i
    elif not (i%A or i%B): # 그 후에는 공배수중에서 제일 먼저 잡히는 애만 잡고 break
        biggest = i
        break
        
print(smallest)
print(biggest)


# ^^ 해답지

# import math
# A, B = map(int, input().split())

# print(math.gcd(A,B))
# print(math.lcm(A,B))