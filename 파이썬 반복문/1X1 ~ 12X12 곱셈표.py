"""
Project : 2중 for-loop을 사용하여 11 ~ 12 12의 곱셈표를 출력하는 파이썬 프로그램을 작성하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""
count = 0

for x in range(1,13):
    for y in range(1,13):
        count += 1
        print("{:2d} x {:2d} = {:3d}, ".format(x, y, x*y),end='') # 들여쓰기를 하고 싶지 않을 때 ,end='' 를 사용
        if count == 12:
            count = 0
            print() # 들여쓰기