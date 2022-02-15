# 5와 6을 헷갈
# 두 수의 가능한 합 중, 최솟값과 최댓값

# '5'랑 '6'을 대체하기위해 for문 돌릴꺼라 문자열로 받음
A, B = input().split()

sA, lA = '', '' # 다 작게 만든 값, 다 크게 만든 값
for num in A:
    if num == '5' or num == '6':
        sA += '5'
        lA += '6'
    else:
        sA += num
        lA += num
sA = int(sA)
lA = int(lA)

sB, lB = '', ''
for num in B:
    if num == '5' or num == '6':
        sB += '5'
        lB += '6'
    else:
        sB += num
        lB += num
sB = int(sB)
lB = int(lB)

print(sA+sB, lA+lB)