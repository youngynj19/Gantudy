'''
루트 없는 트리가 주어진다. 
이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''

import sys
# sys.stdin = open("2.txt")
sys.setrecursionlimit(1000000)

def find_parent(num):
    visited[num] = True
    p = 0 # 부모님을 담을 변수
    for i in tree[num]:
        # 방문한 적 없으면 자식이니까 내려가보고
        # 또 그 자식이 부모님 찾을 때까지 무한 루프 돌다가
        # 다 마쳐서 부모님 찾고 나면 다시 여기로 돌아와서
        # for문에 남은 다른 인덱스 검사하겠지
        if not visited[i]:
            find_parent(i)
        # 방문한 적 있으면 부모님이니까 변수에 저장
        else:
            p = i
    # for문 다 돌았으면 자식도 다 방문하고 더 할 일 없으니까
    # tree 리스트에 부모님만 남기고 너희 부모님 for문으로 돌아가렴 
    tree[num] = p

N = int(input())
tree = [0] + [[] for _ in range(N)]
# 일단 연결된 것들은 다 받기
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)

# 트리 특성상 연결된것들중 하나만 부모
# 부모에게서 자식을 찾으러 내려가기 때문에
# 만약 visited 인 숫자가 있따면 그게 바로 너의 부모님이라는 논리를 이용할 생각
# 그래서 visited 필요
visited = [False for _ in range(N+1)]
find_parent(1)

for i in range(2, N+1):
    print(tree[i])