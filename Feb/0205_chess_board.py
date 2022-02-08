# # 체스판

# # R: 세로 총 칸 수
# # C: 가로 ~
# # A: 칸 높이
# # B: 칸 너비

# # XX..XX..
# # XX..XX..
# # ..XX..XX
# # ..XX..XX

# 밑에 함수 있음!!!!!

R, C = map(int, input().split())
A, B = map(int, input().split())

if R%2: # 홀수번 밑으로 갈 땐 # .......... (4)세로

    for k in range(R//2): # .......... (2)세로

        for j in range(A): # 한 줄 단위 ........ (1/2)세로
            if C%2: # 홀수번 옆으로 갈 땐 ......... 가로(4)
                for i in range(C//2): # .......... 가로(2)
                    print(f'{"X"*B}{"."*B}', end='') # 경험에 의한 결과^^;; ........... 가로(1)
                    # print("X"*B, "."*B, sep='', end='') 
                print('X'*B) # ............ 가로(3)
            else: # 짝수번 옆으로 갈 때 ............ 가로(5)
                for i in range(C//2 -1):
                    print(f'{"X"*B}{"."*B}', end='')
                print(f'{"X"*B}{"."*B}')

        for j in range(A): # 한 줄 단위 ........ (2/2)세로
            if C%2: # 홀수번 옆으로 갈 땐
                for i in range(C//2):
                    print(f'{"."*B}{"X"*B}', end='') 
                print('.'*B)
            else: # 짝수번 옆으로 갈 때
                for i in range(C//2 -1):
                    print(f'{"."*B}{"X"*B}', end='')
                print(f'{"."*B}{"X"*B}')

    for j in range(A): # ............ (3) 세로
            if C%2: # 홀수번 옆으로 갈 땐
                for i in range(C//2): 
                    print(f'{"X"*B}{"."*B}', end='') 
                print('X'*B)
            else: # 짝수번 옆으로 갈 때
                for i in range(C//2 -1):
                    print(f'{"X"*B}{"."*B}', end='')
                print(f'{"X"*B}{"."*B}')

else: # ............... (5) 세로
    for k in range(R//2): # .......... (2)세로

        for j in range(A): # 한 줄 단위 ........ (1/2)세로
            if C%2: # 홀수번 옆으로 갈 땐 ......... 가로(4)
                for i in range(C//2): # .......... 가로(2)
                    print(f'{"X"*B}{"."*B}', end='') # 경험에 의한 결과^^;; ........... 가로(1)
                print('X'*B) # ............ 가로(3)
            else: # 짝수번 옆으로 갈 때
                for i in range(C//2 -1):
                    print(f'{"X"*B}{"."*B}', end='')
                print(f'{"X"*B}{"."*B}')

        for j in range(A): # 한 줄 단위 ........ (2/2)세로
            if C%2: # 홀수번 옆으로 갈 땐
                for i in range(C//2):
                    print(f'{"."*B}{"X"*B}', end='') 
                print('.'*B)
            else: # 짝수번 옆으로 갈 때
                for i in range(C//2 -1):
                    print(f'{"."*B}{"X"*B}', end='')
                print(f'{"."*B}{"X"*B}')












def chess(length, width, height, black, white):
    for j in range(height):
        if length%2: # 홀수번 옆으로 갈 땐 ......... 가로(4)
            for i in range(length//2): # .......... 가로(2)
                print(f'{black*width}{white*width}', end='') # 경험에 의한 결과^^;; ........... 가로(1)
            print(black*width) # ............ 가로(3)
        else: # 짝수번 옆으로 갈 때 ............ 가로(5)
            for i in range(length//2 -1):
                print(f'{black*width}{white*width}', end='')
            print(f'{black*width}{white*width}')

R, C = map(int, input().split())
A, B = map(int, input().split())

if R%2: # 홀수번 밑으로 갈 땐 # .......... (4)세로

    for k in range(R//2): # .......... (2)세로
        chess(C,B,A,'X','.')
        chess(C,B,A,'.','X')
    chess(C,B,A,'X','.')

else: # ............... (5) 세로
    for k in range(R//2): # .......... (2)세로
        chess(C,B,A,'X','.')
        chess(C,B,A,'.','X')