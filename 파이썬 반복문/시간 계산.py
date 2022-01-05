"""
Project : 시간을 나타내는 시 (hour), 분(min), 초(sec)의 3개 정수를 한 줄로 입력 받고, 이 시간이 그날의 0시 0
분 0초로 부터 몇 초가 경과되었는지 계산하고, 그날의 자정 (24:00:00)까지 몇 초가 남았는지 계산하여
출력하는 파이썬 프로그램을 작성하라. 시간의 출력 양식은 (00:00:00) ~ (23:59:59)로 표시할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""
while True:
    time_str = input("input hour min sec : ")
    if time_str == '.':
        break
    hour, min, sec = map(int,time_str.split())
    print("Input time : ({:02}:{:02}:{:02})".format(hour, min, sec))
    print("Elasped seconds from last midnight = {}".format(hour*3600+min*60+sec))
    print("Remaining seconds to next-midnight = {}".format(24*3600-(hour*3600+min*60+sec)))