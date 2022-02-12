# a = [1, 30, 31, 35, 36, 37, 41, 45, 47, 52]

# 80

# 53 = 33
# 82 = 2
# 77 = 3



# 23 25

# 1 8 10// 24 26 41 44 100

# M = 50


N,M = map(int, input().split())
cards = list(map(int, input().split()))




# cards.sort()

# for문에서 하나 빼놓고
# while에서 돌면서 최소값 찾기
# while문 나와서 for문 안에서 이전 card랑 비교하기
# for 다 돌고 가장 작은 거 나오면 for 나와서 출력

# min = 300000
# result = 0
# for cards[i] in cards:
#     cards = cards[:]
#     cards.remove(cards[i])
    
#     s=0
#     e=len(cards)-1 # 투포인터...
#     temp_min = 300000 # M과의 차를 담을 변수, 갈수록 작아짐
#     temp_result = 0
#     while s < e:
#         temp_diff = abs(cards[s]+cards[e]+cards[i] - M)
#         if temp_diff < temp_min:
#             temp_min = temp_diff
#             temp_result = cards[s] + cards[e] + cards[i]
            
#         if temp_min == 0:
#             break
        
#         if cards[s]+cards[e]-M > 0:
#             e -= 1
#         else:
#             s += 1

#     if temp_min < min:
#         min = temp_min
#         result = temp_result
    
#     if min == 0:
#         break
# print(result)






# cards.sort()

# min = 300000
# result = 0
# for i in range(N):

#     s=0
#     e=len(cards) # 투포인터...
#     temp_min = 300000 # M과의 차를 담을 변수, 갈수록 작아짐
#     # while문에서 나온 result(i가 변하면 얘도 바뀔 수 있음)
#     temp_result = 0
#     while s < e:
#         # 0보다 커야하는 값, M과의 차이
#         temp_diff = M - cards[s]+cards[e]+cards[i]

#         # 근데 M보다 합이 크면
#         if temp_diff < 0:
#             e -= 1
#         else: # 지금 차이값이 이전 차이값보다 작으면 없뎃
#             if temp_diff < temp_min:
#                 temp_min = temp_diff
#                 temp_result = cards[s] + cards[e] + cards[i]
#             # 혹시 0일 땐 더 찾아볼 필요 없음    
#             if temp_min == 0:
#                 break
#             s += 1

#     if temp_min < min:
#         min = temp_min
#         result = temp_result
    
#     if min == 0:
#         break
# print(result)






min = 300000
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        if j == i:
            continue
        for k in range(j+1, N):
            if k == j or k == i:
                continue
            temp_result = cards[i]+cards[j]+cards[k]
            temp_min = M - temp_result
            if 0 < temp_min and temp_min <= min:
                min = temp_min
                result = temp_result
print(result)

# [1 30 31 35 36 37 41 45 47 52]