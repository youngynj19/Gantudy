T = int(input())

for tc in range(1, T+1):
    a_lst = list(map(int, input().split()))
    b_lst = list(map(int, input().split()))
    a_lst.pop(0)
    b_lst.pop(0)
    a_lst = sorted(a_lst)
    a_lst.reverse()
    b_lst = sorted(b_lst)
    b_lst.reverse()
    N = min(len(a_lst), len(b_lst))
    flag = 0
    for i in range(N):
        if a_lst[i] > b_lst[i]:
            print('A')
            flag = 1
            break
        elif a_lst[i] < b_lst[i]:
            print('B')
            flag = 1
            break
    if flag == 1:
        pass
    elif len(a_lst) > len(b_lst):
        print('A')
    elif len(a_lst) < len(b_lst):
        print('B')
    else:
        print('D')
