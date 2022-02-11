# 이차방정식의 근
# x^2 + 2AX + B

A,B = map(int, input().split())

X1 = int( -A - (A*A - B)**(0.5) )
print(X1, end=' ')
if A*A != B:
    X2 = int( -A + (A*A - B)**(0.5) )
    print(X2)