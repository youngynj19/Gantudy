# N 번째로 도착한 손님에게 배정될 방 번호를 계산하는 프로그램이다.

T = int(input()) # 테스트 케이스 개수
H, W, N = [], [], [] # 케이스별 각 리스트

for i in range(T): # 각 케이스에 따라 split으로 받고 list에 추가
    h, w, n = map(int, input().split())
    H.append(h)
    W.append(w)
    N.append(n)

# for i in range(T):
#     print(N[i]%H[i], end='') if N[i]%H[i] else print(H[i], end='')  # H 내에서 반복되는 나머지
#     print('0{}' .format(N[i]//H[i] + 1)) if H[i]>1 else print('0{}' .format(N[i])) # H와 연관되서 조금씩 증가하는 몫

for i in range(T):
    for j in range(N[i]):
        ......
