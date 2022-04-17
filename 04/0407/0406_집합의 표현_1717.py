'''
문제
초기에 {0}, {1}, {2}, ... {n} 이 각각 n+1개의 집합을 이루고 있다.
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.

집합을 표현하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 1,000,000), m(1 ≤ m ≤ 100,000)이 주어진다.
m은 입력으로 주어지는 연산의 개수이다. 다음 m개의 줄에는 각각의 연산이 주어진다.
합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다.
이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다. a와 b는 n 이하의 자연수 또는 0이며 같을 수도 있다.

출력
1로 시작하는 입력에 대해서 한 줄에 하나씩 YES/NO로 결과를 출력한다. (yes/no 를 출력해도 된다)
'''

# def find_set(n):
#     while arr[n] != n:
#         n = arr[n]
#     return n
#
#     if arr[n] == n:
#         return n
#     else:
#         return find_set(arr[n])
#
# import sys
#
# N, M = map(int, sys.stdin.readline().rstrip().split())
# arr = [i for i in range(N+1)]
# for _ in range(M):
#     opr, a, b = map(int, sys.stdin.readline().rstrip().split())
#     cnta, cntb = 0,0 # 각 그룹의 레벨을 처리해줄 변수
#     # 미리 find(a), find(b)는 구해놓고
#     # 어짜피 어떤 연산에서든 쓸꺼니까
#     while arr[b] != b:
#         b = arr[b]
#         cntb += 1
#     while arr[a] != a:
#         a = arr[a]
#         cnta += 1
#     # 합집합 연산할 땐
#     # 레벨이 더 큰 애한테 작은애를 접붙혀주자
#     if opr == 0:
#         if cnta > cntb:
#             arr[b] = a
#         else:
#             arr[a] = b
#         # arr[find_set(b)] = find_set(a)
#     elif opr == 1:
#         # if find_set(a) == find_set(b):
#         if a == b:
#             print('YES')
#         else:
#             print('NO')



import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(N+1)]
for _ in range(M):
    opr, a, b = map(int, sys.stdin.readline().rstrip().split())
    # 웬만하면 루트 바로 밑으로 넣게

    # [0, 0, 2, 2]
    # a=1과 b=3을 합친다고 하면
    # 우선 a = 0으로 만들어주고
    # arr[3] 은 a로 만들고
    # arr[3]이 원래 가리키고 있는 2로 가서
    # arr[2]도 걍 a로 만들고
    # [0,0,0,0] 이렇게 하면
    # 웬만한 애들 합쳐도 레벨이 2 이상으로 내려가기는 힘들지 않을까

    # [0,0,3,3,3,3]
    # 에서 1이랑 5를 합친다고 하면
    # [0,0,3,0,3,0] 이렇게 레벨이 3이 될 수도 있지만ㅇㅇ
    if opr == 0:
        while arr[a] != a:
            a = arr[a]
        while arr[b] != a:
            tmp = b
            b = arr[b]
            arr[tmp] = a

    elif opr == 1:
        while arr[b] != b:
            b = arr[b]
        while arr[a] != a:
            a = arr[a]
        if a == b:
            print('YES')
        else:
            print('NO')