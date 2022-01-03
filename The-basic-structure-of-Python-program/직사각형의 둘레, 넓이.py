"""
Project : 직사각형의 가로 (width)와 세로 (length)를 입력 받아 넓이(area)와 둘레(perimeter)를 계산하여 출력
하는 파이썬 프로그램을 작성하고, 실행 결과를 제출하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 3, 2022
"""

width, length = map(int, input("width, length = ").split())
perimeter = 2 * (width + length)
area = width * length

print("Rectangle of width({}) and length({}) : area ({}), perimeter({:.1f})" \
.format(width, length, area, perimeter))