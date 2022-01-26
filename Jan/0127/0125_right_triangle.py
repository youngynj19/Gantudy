# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

triangle = []

while True:
    triangle = list(map(int, input().split()))
    if triangle == [0, 0, 0]:
        break
    else:
        triangle.sort()
        print('right') if triangle[0]**2 + triangle[1]**2 == triangle[2]**2 else print('wrong')