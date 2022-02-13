N = int(input())

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

142
j=0 ... 0(무조건...good)
j=1 ... 0(이진법으로 나눴을 때 1의 값)
...
...
'''

numbers = []
for i in range(N):
    numbers.append(list(map(int, input().split())))

result = 0
for i in range(2**(N-1)):
    summation = 0
    temp = 0
    for j in range(N):
        k = i % (2**j)
        print(i, j, k)
    #     summation += numbers[j][temp+k]
    #     temp = temp+k

    # if summation > result:
    #     result = summation