# 영어 문장과 알파벳 하나가 주어지면
# 그 알파벳이 문장에서 몇 번 나타나는지

in_ls = [] # input 리스트

while True: # '#' 나올때 까지(break) 반복해서 입력 추가
    temp = input()
    if temp == '#':
        break
    in_ls += [temp]

for words in in_ls:
    count = 0 # 알파벳 몇개 나오나??
    for word in words[2::]: # 갹 알파벳을 하나씩 검사, words에서 'a ' 제외
        if word == words[0]:
            count += 1
        elif ord(word) == ord(words[0]) - 32: # 대문자로 바꿔서도 검사!
            count += 1
    print(words[0], count) # 프린트 하고 다음 words 검사