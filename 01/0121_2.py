# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

C = int(input()) # 테스트 케이스 개수
in_ls, out_ls = [], [] # 인풋, 아웃풋 리스트

for i in range(C): # 각 케이스에 따라
    temp = list(map(int, input().split()))
    in_ls += [temp]
# in_ls[i].append(list(map(int, input().split())))
# 각 케이스 학생수 + 점수 받기 ... [i]때문에 안됐더라구요^^;;;

for case in in_ls: # 각 case마다 print
    grades = case[1::] # 점수만 따로 빼서 리스트 만들기
    average = sum(grades)/case[0] # 평균 도출
    count = 0
    for i in grades:
        if i > average:
            count += 1
    rates = count/len(grades) # 평균 이상인 비율 받기
    rates = round(rates*100000) # 소수점 3째자리에서 반올림 하고 
    rates = rates*(1/1000) # 다시 원상복귀
    print('{:0.3f}%'.format(rates)) # 0.3f때문에 엄청 고생했습니다...
