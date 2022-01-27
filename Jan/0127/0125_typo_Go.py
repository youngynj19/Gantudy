# 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 
# 오타를 지운 문자열을 출력

# 4
# 4 MISSPELL
# 1 PROGRAMMING
# 7 CONTESTd
# 3 BALLOON

N = int(input())

for i in range(N):
    test = input()
    typo = int(test[0])
    result = test[2:typo+1]+test[typo+2:]
    print(result)

    # 뭐가 문제일까요?ㅜ 1도 len값도 다 해봤는데...
    # 혹시 띄우면 안되나 해서 그것도 빼봤는데...


# 검색결과
    # num, word = map(str, input().split()) #오답 위치와 word 따로 받기
    # result = ''
    # for i in range(len(word)):
    #     # 오답위치에 가서는 결과에 현재 알파벳 추가 안함
    #     if i == int(num)-1: 
    #         continue
    #     result += word[i]
    # print(result)