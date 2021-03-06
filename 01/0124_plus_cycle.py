# 26부터 시작한다. 2+6 = 8이다. 
# 새로운 수는 68이다. 6+8 = 14이다. 
# 새로운 수는 84이다. 8+4 = 12이다. 
# 새로운 수는 42이다. 4+2 = 6이다. 
# 새로운 수는 26이다.
# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 
# 따라서 26의 사이클의 길이는 4이다.

N = int(input())

# result에 새로운 계산값이 계속 담김
# result를 넣은 이유.. while에서 초기값이랑 계산값이 같으면 
# 반복 종료하는 조건을 만들기 위해서 원본은 살려둬야했어서
result = (N%10)*10 + (N%10 + N//10)%10
# 좌항 수 1의 자리를 10으로 올리고
# + 우항 수(좌항 1의 자리 + 좌항 10의 자리) 1의 자리

# 출력값 count
count = 1 # 결과값 보고 조정^^;;
while result != N:
    count += 1
    result = (result%10)*10 + (result%10 + result//10)%10

print(count)