"""
Project : 표준입력장치 (키보드)로부터 원의 반지름(radius)을 입력 받고, 그 원의 넓이(area)와 원둘레
(circumference)를 출력하는 파이썬 프로그램을 작성하고, 실행 결과를 제출하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 3, 2022
"""
PI = 3.141592 # PI는 상수

radius = int(input("radius =")) # 입력된 문자열을 정수로 사용하기 위해 정수로 바꾼다
area = PI * radius * radius  #원의 넓이
circumference = 2 * PI * radius #원둘레

print("Circle of radius (%d) : area  (%7.3f), circumference (%7.5f)" % (radius, area, circumference))

