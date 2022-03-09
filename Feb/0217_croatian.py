croa = input()

i = 0
cnt = 0
while i < len(croa)-2:
    if croa[i]+croa[i+1]+croa[i+2] == 'dz=':
        cnt += 1
        i += 3
    elif croa[i]+croa[i+1] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1

if len(croa)-i == 2:
    if croa[i]+croa[i+1] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        cnt += 1
        i += 2
    else:
        cnt += 2
        i += 2
else:
    cnt += 1

print(cnt)