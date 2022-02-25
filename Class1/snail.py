# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# x ,y = 0, 0
# dir = 0
# for i in range(25, 1,-1):
#     arr[x][y] = i

#     nx = x + dx[dir]
#     ny = y + dy[dir]

#     if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] != 0:
#         dir = (dir + 1) % 4
    
#     x += dxo[dir]
#     y += dy[dir]





from pprint import pprint

arr = [[0]*5 for _ in range(5)]
n = 5

# di = [1, 0, -1, 0]
# dj = [0, 1, 0, -1]

# i, j = 0, 0
# dir = 0
# for k in range(1, 5*5+1)[::-1]:
#     arr[i][j] = k
#     ni = i + di[dir]
#     nj = j + dj[dir]

#     if not(0<=ni<n and 0<=nj<n) or arr[ni][nj] != 0:
#         dir = (dir+1) % 4

#     i += di[dir]
#     j += dj[dir]

# pprint(arr)

arr = [[0]*5 for _ in range(5)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

i, j = 0, 0
dir = 0
for k in range(1, 26)[::-1]:
    arr[i][j] = k
    ni = i + di[dir]
    nj = j + dj[dir]

    if not(0 <= ni < 5 and 0 <= nj < 5) or arr[ni][nj] != 0:
        dir = (dir+1) % 4
    
    i += di[dir]
    j += dj[dir]

pprint(arr)