N = int(input())
arr = list(map(int, input().split()))

arr.sort()
per_tm, result = 0, 0
for tm in arr:
    per_tm += tm
    result += per_tm
print(result)