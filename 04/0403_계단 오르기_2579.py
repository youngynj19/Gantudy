'''
[10, 20, 15, 25, 10, 20]
[10]
[10, 10+20]
[10, 30, 0+20+15/10+15]
[10, 30, 35, 10+15+25/30+25]
[10, 30, 35, 55, 30+25+10/35+10]
'''

# N = int(input())
#
# stair = [0]
# for _ in range(N):
#     stair.append(int(input()))
#
# if N == 1:
#     print(stair[1])
# else:
#     dp = [0] * (N+1)
#     dp[1] = stair[1]
#     dp[2] = stair[1] + stair[2]
#
#     for i in range(3, N+1):
#         dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
#
#     print(dp[N])












import sys
sys.stdin = open('1.txt')

def find_the_largest_score(i, score, cnt, maxx):
    global result
    if 0<= i <N:
        maxx -= arr[i]
        score += arr[i]
    if i >= N:
        return
    elif score+maxx < result:
        return
    elif i == N-1:
        if result < score:
            result = score
        return
    else:
        if cnt <= 0:
            find_the_largest_score(i+1, score, cnt+1, maxx)
        find_the_largest_score(i+2, score, 0, maxx-arr[i+1])
        # lst.pop(-1)

N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = int(input())
result = 0
maxx = sum(arr)
# lst = []
find_the_largest_score(-1, 0, -1, maxx)
print(result)
















# import sys
# sys.stdin = open('1.txt')
#
# def find_the_largest_score(i, score, cnt):
#     global result
#     if i >= N:
#         return
#     elif i == N-1:
#         print(f'i {i} score {score + arr[i]} cnt {cnt}')
#         score += arr[i]
#         if result < score:
#             result = score
#         return
#     else:
#         print(f'i {i} score {score+arr[i]} cnt {cnt}')
#         if cnt <= 0:
#             find_the_largest_score(i+1, score+arr[i], cnt+1)
#         find_the_largest_score(i+2, score+arr[i], 0)
#
# N = int(input())
# arr = [0] * N
# for i in range(N):
#     arr[i] = int(input())
# result = 0
# find_the_largest_score(-1, 0, 0)
# print(result)