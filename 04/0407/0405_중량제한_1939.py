'''
문제
N(2 ≤ N ≤ 10,000)개의 섬으로 이루어진 나라가 있다. 이들 중 몇 개의 섬 사이에는 다리가 설치되어 있어서 차들이 다닐 수 있다.

영식 중공업에서는 두 개의 섬에 공장을 세워 두고 물품을 생산하는 일을 하고 있다.
물품을 생산하다 보면 공장에서 다른 공장으로 생산 중이던 물품을 수송해야 할 일이 생기곤 한다.
그런데 각각의 다리마다 중량제한이 있기 때문에 무턱대고 물품을 옮길 순 없다.
만약 중량제한을 초과하는 양의 물품이 다리를 지나게 되면 다리가 무너지게 된다.

한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N, M(1 ≤ M ≤ 100,000)이 주어진다.
다음 M개의 줄에는 다리에 대한 정보를 나타내는 세 정수 A, B(1 ≤ A, B ≤ N), C(1 ≤ C ≤ 1,000,000,000)가 주어진다.
이는 A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재한다는 의미이다.
서로 같은 두 섬 사이에 여러 개의 다리가 있을 수도 있으며, 모든 다리는 양방향이다.
마지막 줄에는 공장이 위치해 있는 섬의 번호를 나타내는 서로 다른 두 정수가 주어진다.
공장이 있는 두 섬을 연결하는 경로는 항상 존재하는 데이터만 입력으로 주어진다.

출력
첫째 줄에 답을 출력한다.
'''

# N, M = map(int, input().split())
# arr = [[(-1,-1)] for _ in range(N+1)]
# for _ in range(M):
#     a, b, mass = map(int, input().split())
#     arr[a].append((b, mass))
#     arr[b].append((a, mass))
# # print(arr)
# a, b = map(int, input().split())
# result = 0
# while arr[a]:
#     tmpb, mass = arr[a].pop(0)
#     # print(tmpb)
#     if tmpb == b:
#         result += mass
# print(result)

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [0]
for i in range(N, 0, -1):
    arr.append([0] * i)
# print(arr)
for _ in range(M):
    a, b, mass = map(int, sys.stdin.readline().rstrip().split())
    if a > b:
        a,b = b,a
    arr[a][N-b] += mass
a, b = map(int, sys.stdin.readline().rstrip().split())
if a > b:
    a, b = b, a
print(arr[a][N-b])
    # arr[b].append((a, mass))
# print(arr)
# result = 0
# while arr[a]:
#     tmpb, mass = arr[a].pop(0)
#     # print(tmpb)
#     if tmpb == b:
#         result += mass
# print(result)