
# A, B = map(int, input().split())

# # 최소공배수는 ..... set으로 풀면... 안될 것 같고....
# # 최대공약수는.... 약수 찾아서
# # 최댓값?
# # ㅅㅂ 개어렵네

# A_list, B_list = [], [] # 일단 A, B 모든 약수 모아놓을 리스트
# ########### 인데 중복되는 약수느 ㄴ어떻게?????

# for i in range(1,A+1):
#     if not A%i:
#         A_list += [i]

# for i in range(1,B+1):
#     if not B%i:
#         B_list += [i]
# print(A_list)
# print(B_list)
# # 리스트 둘 다 set으로 묶어서 공집합? 하면 최대공약수는 구할 듯

# A_and_B = set(A_list) & set(B_list)
# # A_or_B = set(A_list) | set(B_list)

# print(max(A_and_B))
# # print(A_or_B)

# AB_list = [] # A*B의 모든 약수
# for i in range(1,A*B+1):
#     if not (A*B)%i:
#         AB_list += [i]

# AB_bigger = [] # A와 B의 공배수
# for num in AB_list:
#     if not (num%A or num%B): # 둘 중 하나라도 1이면 괄호가 1 -> 0
#         AB_bigger += [num]
# print(min(AB_bigger))

# ########### set에서 제일 큰 애가 최대 공약수인가????? 맞음

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







# A, B = map(int, input().split())

# smallest = 0
# biggest = 0 
 
# for i in range(1,A*B+1):
#     if not (A%i or B%i):
#         smallest = i
#     elif not (i%A or i%B):
#         biggest = i
#         break
        
# print(smallest)
# print(biggest)

import math
A, B = map(int, input().split())

print(math.gcd(A,B))
print(math.lcm(A,B))