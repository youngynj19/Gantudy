# # 경우의수
# # 1X
# # 2X
# # 2X
# # 2X
# # 2
# # = 2^4
# # = 2^(n-1)

# # [[0],[0,1],[0,1,2],[0,1,2,3],...,[0,...,n]]
# # 본인 or 본인+1
# # 이거 ttt ttf tft tff ftt ftf fft fff 이렇게 하는 문제임

# N = int(input())

# numbers = []
# for i in range(N):
#     numbers.append(list(map(int, input().split())))

# result = 0
# for i in range(2**(N-1)): # 총 경우의 수에 대해
#     # 카운터를 넣어서
#     # 카운터 하나가 증가할때마다
#     # j문 안쪽에서 if문 처리한 다음에 k가 올지 k+1올지 결정
#     # 이전 k 받아줄 변수 하나
#     # k일지 k+1일지 결정해줄 변수 하나
#     summation = 0
#     k = i
#     m = 0
#     l = 0
#     for j in range(N):
#         m = m + l # 첫 번째 m은 무조건 0
#         # print(i, j, m, "*****", k, l)
#         summation += numbers[j][m]
#         l = k % 2 # 그 뒤로 2진법으로 바꾼 수의 첫째자리 ~ n-1째자리까지
#         # 만약 0이면 다음 인덱스도 그대로 1이면 1증가한 인덱스
#         k = k // 2

#     if summation > result:
#         result = summation
# print(result)








'''
input 받은 값을 전에 받은 값에다가 그대로 더하게
인풋+를 쌓아둘 리스트
인풋을 받을 리스트

인풋+ : 1, 2, 4, 8 ,16
인풋 : 1, 2, 3, 4, 5

인풋[0]
인풋+[0]

인풋[1]
인풋+ for문 돌면서



1층 - 2^0
2층 - 2^1
3층 - 2^2
4층 - 2^3
n층 - 2^(n-1)

'''

N = int(input())

numbers = [int(input)]
for i in range(N): # N = 5
    temp_numbers = []
    temp = list(map(int, input().split()))
    print('t:',temp)
    for j in range(len(numbers)):
        temp_numbers.append(numbers[j]+temp[(j+1)//2])
        if i != 0:
            temp_numbers.append(numbers[j]+temp[((j+1)//2)+1])
    numbers = temp_numbers
    print('n:',numbers)
print(max(numbers))









# 경우의수
# 1X
# 2X
# 2X
# 2X
# 2
# = 2^4
# = 2^(n-1)

# [[0],[0,1],[0,1,2],[0,1,2,3],...,[0,...,n]]
# 본인 or 본인+1
# 이거 ttt ttf tft tff ftt ftf fft fff 이렇게 하는 문제임

# 이중for문ㄱㄱ
# 실패

# 첫 for문에서 각 층 들어가면서 더해줄 준비

# 됐고 경우의수는 아니까 각 경우의 수마다 길 만들어주자
# 그리고 그걸 그냥 대입하셈

# 0,0 1,0 2,0 3,0 4,0
# 0,0 1,0 2,0 3,0 4,1
# 0,0 1,0 2,0 3,1 4,1
# 0,0 1,0 2,0 3,1 4,2
# 0,0 1,0 2,1 3,1 4,1
# 0,0 1,0 2,1 3,1 4,2
# 0,0 1,0 2,1 3,2 4,2
# 0,0 1,0 2,1 3,2 4,3

# i, j, k
# k는 j or j+1
# i가 1~5까지 돌면
# i=0 .. j=0
# i=1 .. j=0or1 
# i=2 .. j=0~2
# i는 지금 더하고 있는 값
# 근데 도는걸 보면 ...

# i가 다섯 번 도는 동안[i][j]
# j의 지난 값이 지금 j에 영향을 미쳐야함
# for i in range(N):
#     
#     for j in range(i):
#         k = j

# 층수를 순회하는게 제일 밑에 와야함
'''
for j in range(i):
    for k in range(j,j+2):
        for i in range(5):
            summation += numbers[i][j]


maximum
while:

    summation = 0
    for i in range(5):
        summation += numbers[i][j]
    
    if summation > maximum:
        maximum = summation


0
0
0
0
0

0
0
0
0
1

0
0
0
1
1

0
0
0
1
2

...

0
0
0
4
4

0
0
0
4
5



카운터를 넣어서
카운터 하나가 증가할때마다
j문 안쪽에서 if문 처리한 다음에 k가 올지 k+1올지 결정
이전 k 받아줄 변수 하나
k일지 k+1일지 결정해줄 변수 하나

for i in range(2**(N-1)):


    summation = 0
    temp = 0
    for j in range(N):
        summation += numbers[j][k]
        temp = k




result = 0
for i in range(2**(N-1)):


    summation = 0
    temp = 0
    for j in range(N):
        k = i % (2**j)
        summation += numbers[j][temp+k]
        temp = temp+k

    if summation > result:
        result = summation 

i=142 ... % 2**j
j=0 ... 0(무조건...good)
j=1 ... 0(이진법으로 나눴을 때 1의 값)
j=2 ... 2(0~3)
j=3 ... 6(0~7)




result = 0
for i in range(2**(N-1)):


    summation = 0
    temp = 0
    k = i
    m = 0
    for j in range(N):
        l = k % 2
        m = m + l
        summation += numbers[j][m]
        k = k // 2

    if summation > result:
        result = summation

i = 145 ... % j
...
'''


    

    # if summation > result:
    #     result = summation