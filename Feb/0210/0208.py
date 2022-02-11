# 개 한마리는 A분동안 공격적이고, B분동안 조용히 쉬고 있다. 
# 또다른 개는 C분동안 공격적이고, D분동안 조용히 쉰다
# 세명의 의 도착 시간이 주어졌을 때, 각각 개 몇 마리에게 공격을 받는지

dogs = list(map(int, input().split()))
men = list(map(int, input().split()))

for man in men:
    attacked = 0
    for i in range(0,3,2):
        attacked += int( (man%(dogs[i]+dogs[i+1]) <= dogs[i]) and (man != dogs[i]+dogs[i+1]) )
    print(attacked)