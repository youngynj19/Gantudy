# 준서는 길이가 L인 염기열을 가지고 있는데, 
# 이 염기열에서 각 1개씩의 ‘A’, ‘C’, ‘G’, ‘T’ 염기를 빼내
# 완전히 같은 위치의 네 염기로 이루어진 게 아니라면 서로 다른 성질의 피노키오
# 피노키오의 종류가 총 몇 개

# 왜 안나올까요...####

N = int(input()) # 필요도 없는듯;;;
gene = input()
# ACGT = [gene.count('A'), gene.count('C'), gene.count('G'), gene.count('T')]

# result = 1
# for count in ACGT:
#     result *= count if count > 0 else 1
# print(result)
print((gene.count('A')*gene.count('C')*gene.count('G')*gene.count('T'))%1000000007)