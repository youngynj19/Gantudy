def search_to_flute(i, j):
    global count
    global result
    # 현재 라운드에서 visit한 장소로 돌아왔을 땐 한 곳에 만들어줘야!
    if visited[i][j] == count:
        result += 1
        return
    # visit한 적이 있는 곳으로 왔긴 했는데 현재라운드는 아니다
    # 그럼 굳이 result 추가 안해도 되고 이전 라운드에 버스타고 걍 종료
    elif visited[i][j]:
        return
    # 아직 visit한 적이 없는 곳이라면
    else:
        visited[i][j] = count

    # 이제 움직이자
    if arr[i][j] == 'U':
        search_to_flute(i-1, j)
    elif arr[i][j] == 'D':
        search_to_flute(i+1, j)
    elif arr[i][j] == 'L':
        search_to_flute(i, j-1)
    elif arr[i][j] == 'R':
        search_to_flute(i, j+1)
    return


N, M = map(int, input().split())

arr = ['' for _ in range(N)]
for i in range(N):
    arr[i] = input()
# print(arr)

visited = [[0 for _ in range(M)] for _ in range(N)]
# print(visited)

count = 1 # 현재 라운드
result = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        # print(i, j)
        search_to_flute(i, j)
        count += 1

print(result)