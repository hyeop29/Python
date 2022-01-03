"""
Project : 표준입력장치 (키보드)로부터 직사각형의 가로 (width) 및 세로 (length) 크기를 각각 입력 받고, 터틀
그래픽을 사용하여 지정된 크기의 사각형을 (0, 0) 좌표가 중심이 되도록 그리는 파이썬 프로그램을 작
성하고, 실행 결과를 제출하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 3, 2022
"""
import turtle

width = int(input('width = ')) #가로 입력
length = int(input('length = ')) #세로 입력

turtle.setup(500,500) #set width and height of canvas
t = turtle.Turtle()
t.shape('turtle')
t.pencolor('red')
t.width(10) # 선 굵기

t.up();t.goto(-width/2, -length/2);t.down() # 펜을 들어서 옮기기

count = 0
while count < 2:
    count += 1
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)

t.up();t.goto(0, 0);t.down # 펜을 들어서 옮기기







