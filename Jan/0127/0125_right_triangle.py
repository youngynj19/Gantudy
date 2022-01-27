# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

triangle = [] # sort쓰려고 리스트에 담기

while True:
    triangle = list(map(int, input().split()))
    if triangle == [0, 0, 0]: # 종료조건
        break
    else:
        triangle.sort()
        # 조건식이 너무 길어져서 변수로 대체(가독성)
        right = triangle[0]**2 + triangle[1]**2 == triangle[2]**2
        print('right') if right else print('wrong')