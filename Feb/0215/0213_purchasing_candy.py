# 지폐의 액면가는 항상 1, 10, 100, 1000, ..., 1,000,000,000 중 하나이다. 
# 또, 지폐를 무한개 가지고 있다
# 상근이가 지불할 수 있는 가장 가까운 금액으로 사탕의 가격을 반올림

candy, money = map(int, input().split())

# 걍... 수학계싼
if candy%(10**money) >= 5*(10**(money-1)):
    print((candy//(10**money)+1)*(10**money))
else:
    print((candy//(10**money))*(10**money))