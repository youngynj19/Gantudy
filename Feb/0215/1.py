

# 문제를 오해해서 헤메다가 인터넷에 답찾아보고 아차싶었음^^;;;
# 실절적 문맹률이 문제다

A,B,C = map(int, input().split())

drink = 0
while (A+B)//C > 0:
    drink += (A+B) // C
    A, B = (A+B) % C, (A+B) // C

print(drink)