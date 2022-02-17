N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 리스트에서 한 인덱스씩 조회하는데
# 해당 인덱스에서부터 뒤로 하나씩 더해가다가 일치하면 cnt!
# 커지면 while문 벗어나게
# 또 인덱스 벗어나도 while문 벗어나게

cnt = 0
i = 0
while i < N:
    index = i
    temp = 0
    while index < N:
        temp += nums[index]
        if temp == M:
            cnt += 1
        elif temp > M:
            break
        else:
            index += 1   
    i += 1
print(cnt)













# N, M = map(int, input().split())
# nums = list(map(int, input().split()))

# # 리스트에서 한 인덱스씩 조회하는데
# # 해당 인덱스에서부터 뒤로 하나씩 더해가다가 일치하면 cnt!
# # 커지면 while문 벗어나게
# # 또 인덱스 벗어나도 while문 벗어나게


# def is_summation_target_from_index(index, target, ls):
#     temp = 0
#     while index < len(ls):
#         temp += nums[index]
#         if temp == target:
#             return 1
#         elif temp > M:
#             return 0
#         else:
#             index += 1
#     return 0


# cnt = 0
# i = 0
# while i < N:
#     cnt += is_summation_target_from_index(i, M, nums)
#     i += 1
# print(cnt)