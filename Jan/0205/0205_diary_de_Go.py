# 남들이 자신의 일기장을 보는 것을 막기 위해 모음 다음에 'p'를 하나 쓰고, 그 모음을 하나 더 쓴다.
# 원래 문장은 무엇인지 구하는 프로그램을 작성하시오.

diary = input()
vowl = ['a', 'i', 'o', 'u', 'e']
new_diary = ''

# 오리지날은 for 돌리는데 계속 놔두고
# 새거에 넣을꺼야 오리지날에서 안넣기도 하면서
# index로 받으면서 혹시 빼먹는거 생기면 
# index 올라가는거에서 빼먹게 하자

# i = 0
# # length = len(diary)
# while i < len(diary):
# #     # encription = chr+'p'+chr
# #     # new_diary += encription if chr in vowl else chr
#     # 같은 모음이 나오고 and 중간에 p가 있으면
#     if (diary[i] == diary[i+2] in vowl) and (diary[i+1] == 'p'):
#         new_diary = diary[i]
#         i += 2
#         # len -= 2
#     i += 1


# two, one = '', ''
# for chr in diary:
#     if two == chr in vowl and one == 'p':
#         two, one = '', ''
#     else:
#         new_diary += two
#     two, one = one, chr
# new_diary += two + one
# 얘는 epe를 암호화했을 때 나오는 epepepe에 취약함


# [ ][ ][ ]
# zepelepenapa papapripikapa
# [ ][ ][z]epelepenapa papapripikapa
# [ ][z][e]pelepenapa papapripikapa
# [z][e][p]elepenapa papapripikapa
# ...
# [e][l][e]penapa papapripikapa
# [l][e][p]enapa papapripikapa
# [e][p][e]napa papapripikapa
# [e][ ][ ]napa papapripikapa
# ...
# [k][a][p]a
# [a][p][a]

two, one, this = '', '', '' # 문자열을 읽어들어가면서 뒤에 있는 두 번째까지 
for chr in diary:
    two, one, this = one, this, chr
    new_diary += two
    if two == chr in vowl and one == 'p':
        this, one = '', ''
    # two, one = one, chr
new_diary += one + this


print(new_diary)
# new_diary += diary[]