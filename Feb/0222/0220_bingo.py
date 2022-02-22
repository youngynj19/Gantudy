def mark_on_bingo_board(K, bingo):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == K:
                return i, j

def find_bingo(bingo):
    result = 0
    dia1, dia2 = 0, 0
    for i in range(5):
        hor, ver = 0, 0
        for j in range(5):
            if bingo[i][j] == 0:
                hor += 1
            if bingo[j][i] == 0:
                ver += 1
        if hor == 5:
            result += 1
        if ver == 5:
            result += 1
        if bingo[i][4-i] == 0:
            dia1 += 1
        if bingo[i][i] == 0:
            dia2 += 1
    if dia1 == 5:
        result += 1
    if dia2 == 5:
        result += 1
    
    return result
        

bingo = [list(map(int, input().split())) for _ in range(5)]
answer = []
for _ in range(5):
    answer += list(map(int, input().split()))

for i in range(25):
    ii, jj = mark_on_bingo_board(answer[i], bingo)
    bingo[ii][jj] = 0
    if i >= 11:
        if find_bingo(bingo) >= 3:
            print(i+1)
            break
        
