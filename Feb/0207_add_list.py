# 정렬되어있는 두 배열 A와 B가 주어진다. 
# 두 배열을 합친 다음 정렬해서 출력

N, M = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

print(*sorted(list_A+list_B))