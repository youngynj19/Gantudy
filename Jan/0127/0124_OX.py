# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

N = int(input())

for i in range(N):
    ox = input()
    result, stack = 0, 1 # result, stack 초기화, stack은 O를 만날 때마다 1씩 증가시켜줄 예정
    for element in ox:
        if element == 'O':
            result += stack 
            # O를 만날 때마다 늘어나는 stack을 담아줍니다. 
            # 이전이 O였으면 2가 담기고, 2연속 O였으면 3이 담기게
            stack += 1
        else:
            stack = 1 # X를 만나면 stack은 1로 초기화
    print(result)