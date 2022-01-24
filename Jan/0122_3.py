# 원래 설정되어 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.

hour, minute = map(int, input().split())

minute = minute - 45 # 분 먼저 계산 후 조건을 분석 시작
if 0 > minute:
    minute += 60
    hour = hour-1 if hour > 0 else 23 # 분이 음수가 되었으면 hour도 바뀌어야함

print(hour, minute)