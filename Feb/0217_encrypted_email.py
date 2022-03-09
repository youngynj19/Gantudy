# 원문의 전체 길이의 두 약수중 가장 차가 작은 값
# 둘은 같아도 된다
# 긴걸 행으로, 짧은걸 열로
# 행에다가 쭉 쓰고 다음열...
# 이제 각 열의 1행 쭉 읽고
# 각열의 2행 쭉 읽고 하는식으로 암호문 만듦
# 해독 코드 만들어라

encrypted = list(map(str, input()))
length = len(encrypted)

RC = []
for i in range(1, length+1):
    if length % i == 0:
        RC += [i]

R, C = 0, 0
if len(RC) % 2:
    R = C = RC[len(RC)//2]
else:
    R = RC[len(RC)//2-1]
    C = RC[len(RC)//2]

for i in range(R):
    for j in range(C):
        # print(j*R + i%R, end =' ')
        print(encrypted[j*R + i], end ='')