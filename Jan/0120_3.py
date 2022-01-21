# 성냥이 박스에 들어가려면, 박스의 밑면에 성냥이 모두 닿아야 한다.
# 박스의 크기와 성냥의 길이가 주어졌을 때, 
# 성냥이 박스에 들어갈 수 있는지 없는지를 구하는 프로그램을 작성하시오. 창영이는 성냥을 하나씩 검사한다.

N, W, H = map(int, input().split()) # 성냥 갯수, 가로, 세로
stick = [] # 성냥 길이 list
for i in range(N): # N만큼 인풋 받기
    stick += [int(input())]

for i in stick:
    if i*i <= W*W + H*H: # 피타고라스 정리 이용해서 조건 설정 후 프린트
        print("DA")
    else:
        print("NE")
