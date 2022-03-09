# N장의 카드 중에서 3장의 카드를 골라야 한다. 
# 카드의 합은 M을 넘지 않으면서 
# M과 최대한 가깝게

N,M = map(int, input().split())
cards = list(map(int, input().split()))





# 1번 방법: 투포인터

cards.sort()

min = 300000
result = 0
# 값이 세개라서 첫 번째 값은 for문에서 받음
for i in range(N):

    # 이제 투포인터 받을 준비
    s=0
    e=len(cards)-1
    temp_min = 300000 # M과의 차를 담을 변수, 갈수록 작아짐
    temp_result = 0 # while문에서 나온 result(i가 변하면 얘도 바뀔 수 있음)
    while s < e:
        # 0보다 커야하는 값, M과의 차이
        temp_diff = M - (cards[s]+cards[e]+cards[i]) 

        # 근데 M보다 합이 크면
        if temp_diff < 0:
            e -= 1
        # 지금 차이값이 이전 차이값보다 작으면 없뎃
        else: 
            # i랑 같으면 안되니까 바로 s만 커지게, e의 경우엔 애초에 result에 들어갈 필요가 없어서 여기 넣음
            if s==i or e==i:
                pass
            # temp_min이랑 비교하는 이유는 i가 변하면 얘도 바뀔 수 있기때문. 그래서 애초에 for문 안쪽에서 선언함
            elif temp_diff < temp_min:
                temp_min = temp_diff
                temp_result = cards[s] + cards[e] + cards[i]
            # 혹시 0일 땐 더 찾아볼 필요 없음    
                if temp_min == 0:
                    break
            s += 1
    # <지금 while문에서의 resul>랑 <이전 while문에서의 result> 비교
    # 만약 temp_min이 0이면 min도 0이 됨 - 밑에서 break
    if temp_min < min:
        min = temp_min
        result = temp_result
    
    if min == 0:
        break
print(result)




# # 2번 방법 : 삼중for문^^

# min = 300000
# result = 0

# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             # print(cards[i], cards[j], cards[k])
#             temp_result = cards[i]+cards[j]+cards[k]
#             temp_min = M - temp_result
#             if (0 <= temp_min) and (temp_min <= min):
#                 min = temp_min
#                 result = temp_result
#                 # print('*********temp result*********', temp_result)
# print(result)








# a = [1, 30, 31, 35, 36, 37, 41, 45, 47, 52]

# 80

# 53 = 33
# 82 = 2
# 77 = 3



# 23 25

# 1 8 10// 24 26 41 44 100

# M = 50