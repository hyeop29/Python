"""
Project : 정 삼각형의 한 변의 길이 (length)를 입력 받고, 터틀 그래픽 화면 중앙에 정삼각형을 그리
는 파이썬 프로그램을 작성하라. 삼각형의 좌측 하단 꼭지점의 좌표를 정확하게 계산하여 출
력하며, 터틀 그래픽의 중앙과 정 삼각형의 각 꼭지점 좌표를 터틀 객체의 write() 함수를 사
용하여 출력할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""
import turtle, math

length = int(input("input side length of triangle = ")) #정삼각형의 한변의 길이 입력 받기

x0 = -length/2
print(math.pi/6)
y0 = math.tan(math.pi/6) * x0

print("x0, y0 = {} {}".format(x0, y0))

turtle.setup(500,500) #set width and height of canvas
t = turtle.Turtle()
t.shape('turtle')
t.pencolor('red')
t.width(10) # 선 굵기

t.up();t.goto(x0, y0);t.down() # 펜을 들어서 옮기기

for i in range(3):
    t.forward(length)
    t.left(120)

t.up();t.goto(0, 0);t.down() # 펜을 들어서 옮기기

while True:
    x = input("콘솔창을 닫으실려면 x를 누르세요: ")
    if x == 'x':
        break
