#  각 문자를 R번 반복해 새 문자열 출력

N = int(input())

for i in range(N):
    test = input()
    result = ''
    for chr in test[2:]: # sweap? 으로 for문 돌리기
        result += chr*int(test[0])
    print(result)