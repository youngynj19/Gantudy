# 2009년 날짜가 주어졌을 때, 무슨 요일인지 출력하는 프로그램을 작성하시오.


D, M = map(int, input().split())

# 목요일부터

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

index = 2 # 수요일(2008/12/31)
# while 시작하면 목요일부터 시작하게
# index % 7 할 생각

for i in range(M):
    if i in [1, 3, 5, 7, 8, 10]: # 해당 월의 전 달
        index += 31
    elif i in [4, 6, 9, 11]:
        index += 30
    elif i==2:
        index += 28
        
index += D

print(day[index % 7])