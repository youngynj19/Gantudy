words = input()

stop = False
temp = ''
for word in words:
    if stop:
        print(word,end='')
        if word == '>':
            stop = False
    else:
        if word == '<':
            print(temp[::-1],end='<')
            temp = ''
            stop = True
        elif word == ' ':
            print(temp[::-1],end=' ')
            temp = ''
        else:
            temp += word
print(temp[::-1])
