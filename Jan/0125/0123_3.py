M, N = int(input().split())
# N-1 1
# M-1 2
# N-1 3
# M-2 4
# N-2 5
# M-3 6
# N-3 7
# M-4 8
# ...
# 1   X

# N = 2 or M = 2 ... 2
# M = 3 ... 4
# N = 3, M > 3 ... 5

count = 1
while N:
    M -= 1
    count += 1
    if not M:
        break
    N -= 1
    count += 1
print(count)


