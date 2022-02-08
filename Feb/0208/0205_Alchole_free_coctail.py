# 오렌지, 사과, 파인애플 주스의 양 A, B, C
# 칵테일을 만드는데 필요한 각 주스의 비율 I, J, K
# 칵테일을 최대한 많이 만들었을 때, 각 주스가 얼만큼 남는지

juice = list(map(int, input().split()))
proportion = list(map(int, input().split()))


# 일단 나눠보자 - 리스트에 저장
coct = list()
for i in range(3):
    coct.append(float(f'{juice[i]/proportion[i]:f}'))

# 10   16   18 ... 주스
# 3    4    1 ... 비율
# 3.3  3.7  18 ... 주스/비율 ... 1)

# 10   13.2 3.3 ... 1)*비율 ... 2)
# 0    1.66 14.6 ... 주스 - 2)
# 나눈 값중 최소값을 다른 주스비에 곱해서 해당 주스에서 빼줌!
remain = []
for i in range(3):
    if abs(coct[i]-min(coct)) < 1e-8:
        remain.append(0)
    else:
        remain.append(juice[i]-(min(coct)*proportion[i]))
print(*remain)