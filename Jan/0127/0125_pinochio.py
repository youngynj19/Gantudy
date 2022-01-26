N = int(input())
gene = input()
ACGT = [gene.count('A'), gene.count('C'), gene.count('G'), gene.count('T')]

def factorial(num):
    if num <= 1:
        return num
    else:
        return num*factorial(num-1)

print(cases)
for i in range(4):
    cases = cases//factorial(ACGT[i])

print(1000000007%cases)

# 문제가 잉해가 안됨....