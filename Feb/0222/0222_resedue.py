arr = [int(input()) for _ in range(10)]

result = set()
for i in range(10):
    result |= {arr[i]%42}

print(len(result))