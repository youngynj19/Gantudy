'''
문제
해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에, N과 M이 들어온다. N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.
'''
# 부모?? 에서 자식으로 내려가면서 각 컴퓨터가 해킹할 수 있는 갯수 체크 
# N개를 돌면서 각 컴퓨터를 다 체크
# 근데 혹시 방문한 곳을 또 들어가게 된다? 
# 그 뜻은 니가 그 친구의 부모라는거니까 멈추고 걔한테 저장된 갯수 받으셈 

import sys
# sys.stdin = open('1.txt')
sys.setrecursionlimit(1000000)

def how_many_can_you_hack(node):
    # 이미 전에 계산해놓은 자손 개수가 있으면 바로 리턴
    if tree[node][0]:
        return tree[node][0]
    # 없다면(0이라면) 이제 모든 자식들 세면서 비교ㅇㅇ
    else:
        # 일단 나 세주고
        tree[node][0] += 1
        # 자식들도 세주고
        for ci in range(1, len(tree[node])):
            tree[node][0] += how_many_can_you_hack(tree[node][ci])
        return tree[node][0]

N, M = map(int, input().split()) # 노드, 간선
# [[0], [0,4,5,2], [0,3], [0,4,7], [0,7], ...]
# 자식을 나를 신뢰하는 노드들로 넣을 예정
# 부모님이 여럿이 될 수도 있고, 서로가 부모이자 자식일 수도 있겠찌만 뭐 걍 그럴 생각
# tree[n][0]는 얘가 신뢰하는 컴 전부를 본인 포함해서 넣을 예정
tree = [[0] for _ in range(N+1)]
for _ in range(M):
    c, p = map(int, input().split())
    tree[p].append(c)

cnt = 0 # 해킹할 수 있는 컴 수
lst = [] # 출력할 리스트
for node in range(1, N+1):
    temp = 0
    # 해당 노드의 밸류값이 없다면(방문한 적이 없다면)
    if not tree[node][0]:
        temp = how_many_can_you_hack(node)
    if cnt < temp:
        cnt = temp
        lst = [node]
    elif cnt == temp:
        lst.append(node)

lst.sort()
print(*lst) 