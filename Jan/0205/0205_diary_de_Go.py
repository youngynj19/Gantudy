
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

two, one = '', ''
for chr in diary:
    if two == chr in vowl and one == 'p':
        two, one = '', ''
    else:
        new_diary += two
    two, one = one, chr
new_diary += two + one


print(new_diary)
# new_diary += diary[]