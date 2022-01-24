# 암호화하려는 문장 (평문)의 단어와 암호화 키를 숫자로 바꾼 다음, 
# 평문의 단어에 해당하는 숫자에 암호 키에 해당하는 숫자를 빼서 암호화

# print(ord(' ')) = 32

msg, key = input(), input() # input 받기
key_num = [] # key 문자열을 수열로 고치기
for word in key:
    key_num += [ord(word)-96]
# 'a' = 97이므로 모든 아스키코드에서 96을 빼면 'a' = 1부터 정렬 가능

count = -1 # key 수열을 읽어들일 index
for word in msg:
    count += 1 # range(msg길이)
    indexing = count % len(key_num) # key 수열 index를 계속 0부터 반복하게
    number = ord(word)-96 # 메세지 각 알파벳 대응 숫자
    number = number - key_num[indexing] # 일단 앞당기기
    number += 96 if number > 0 else 26 + 96
    # number를 다시 아스키코드값으로 변환(음수는 z까지 끌올)
    # 공백 ... 32-96 ... 최대값: 32-96-1(a) = -65
    # 알파벳 최소값: 1(a) - 26(z) = -25
    # 공백 반환 숫자 최대값 = -65+96+26 = 57
    if number < 60:
        number = 32 
    print(chr(number), end='')