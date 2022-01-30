N = int(input())

for i in range(N):
    test_case = input()
    # 딕셔너리에 넣고
    # sort 해서 - sort 함수 없습니다^^
    # 맨 뒤
    # 바로 앞이랑 비교해서 '?' 출력
    # 공백도 처리
    dic = {}
    for char in test_case:
        # 이미 알파벳이 나온 경우: 해당 키에 하나 더해준다
        if char in dic: 
            dic[char] += 1
        # 처음 나오는 알파벳 : 딕셔너리에 추가한다
        else:
            dic = dic | {char: 1}
            # 할당해야하는지 아님 원본이 바뀌는지 헷갈리지 말기ㅜ
    # 첫 번째로 큰 값, 두 번째로 큰 값 - 나중에 비교하려고
    first, second = ['', 0], ['', 0]
    for key, value in dic.items():
        if key == ' ': # if는 무시
            continue
        elif value >= first[1]:
            # 큰 값이 나왔으면 first, second 교체
            # 같은 값이 나와도 first, second 업뎃해서 '?' 뽑을 수 있게 
            first, second = [key, value], first
    if first[1] == second[1]:
        print('?')
    else:
        print(first[0])