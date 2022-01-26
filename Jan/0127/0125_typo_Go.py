# 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 
# 오타를 지운 문자열을 출력

N = int(input())

for i in range(N):
    test = input()
    typo = int(test[0])
    # print(f'{test[2:typo+1]}{test[typo+2:]}')
    print(test[1:typo]+test[typo+1:])

    # 뭐가 문제일까요?ㅜ 1도 len값도 다 해봤는데...
    # 혹시 띄우면 안되나 해서 그것도 빼봤는데...