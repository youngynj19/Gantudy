N = int(input())
seats = input()

couple = 0
for s in seats:
    if s == 'L':
        couple += 1
couple_die = couple//2 - 1
print(N - couple_die)