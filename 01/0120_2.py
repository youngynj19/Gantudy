# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

A, B, C = map(int, input().split())
new_list = [A, B, C] # sorting 한 후 [1]값 반환할 예정

if new_list[0] > new_list[1]:
    new_list[0], new_list[1] = new_list[1], new_list[0]
if new_list[1] > new_list[2]:
    new_list[1], new_list[2] = new_list[2], new_list[1]
# [2]이 자리정리 완료된 [1]보다 크면 문제X
# 근데 [2]가 [1]보다 작아서 자리가 바뀌었다면 -> [0]보다 작을 경우의 수도 고려해야함
if new_list[0] > new_list[1]:
    new_list[0], new_list[1] = new_list[1], new_list[0]

print(new_list[1])
    

# 처음 시도한 코드    
# if A > B:
#     if C > A:
#         print(A)
#     elif B > C:
#         print(B)
#     else:
#         print(C)
# else:
#     if C > 