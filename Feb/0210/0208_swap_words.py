T = int(input())

for tc in range(T):
    words = list(input().split()) # word들 따로 떼서 저장
    length = len(words)
    result = ''
    for i in range(length):
        result += words[length-1-i] + ' '
    print(f'Case #{tc+1}: {result}')