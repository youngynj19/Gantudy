n = int(input())

# 엄지-검지-중지-약지-아기-약지-중지-검지 까지가 한 세트
# 그 뒤로는 저 여덟단계 반복
# 반복되는 수열은 % 연산자를 통해 답을 얻을 수 있음
# ex) 중지는 8로 나누었을때 나머지가 3인 수 or 나머지가 7인 수의 집합 
if  n % 8 == 1:
    print(1)
elif (n % 8 == 2) or (n % 8 == 0):
    print(2)
elif (n % 8 == 3) or (n % 8 == 7):
    print(3)
elif (n % 8 == 4) or (n % 8 == 6):
    print(4)
else:
    print(5)