# 난쟁이...

import copy

dwarfs = []
for i in range(9):
    dwarfs.append(int(input()))
# A = B[:]

for i in range(8):
    first_dwarfs = copy.copy(dwarfs)
    stop = 0
    first_dwarfs.remove(first_dwarfs[i])
    for j in range(i,8):
        second_dwarfs = copy.copy(first_dwarfs)
        # print(dwarfs[i], dwarfs[j])
        second_dwarfs.remove(second_dwarfs[j])
        if sum(second_dwarfs) == 100:
            
            for dwarf in sorted(second_dwarfs):
                print(dwarf)
            stop = 1
            break
    if stop:
        break
