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

min = 300000
result = 0
# for card in cards:
#     new_cards = cards[:]
#     new_cards.remove(card)
    
#     s=0
#     e=len(new_cards)-1 # 투포인터...
#     temp_min = 300000 # M과의 차를 담을 변수, 갈수록 작아짐
#     temp_result = 0
#     while s < e:
#         temp_diff = abs(new_cards[s]+new_cards[e]+card - M)
#         if temp_diff < temp_min:
#             temp_min = temp_diff
#             temp_result = new_cards[s] + new_cards[e] + card
            
#         if temp_min == 0:
#             break
        
#         if new_cards[s]+new_cards[e]-M > 0:
#             e -= 1
#         else:
#             s += 1

#     if temp_min < min:
#         min = temp_min
#         result = temp_result
    
#     if min == 0:
#         break



for i in range(N):
    for j in range(N):
        if j == i:
            continue
        for k in range(N):
            if k == j or k == i:
                continue
            temp_result = cards[i]+cards[j]+cards[k]
            temp_min = abs(temp_result - M)
            if temp_min <= min:
                min = temp_min
                result = temp_result
print(result)

# [1 30 31 35 36 37 41 45 47 52]