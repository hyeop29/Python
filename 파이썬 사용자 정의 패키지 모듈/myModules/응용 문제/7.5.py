"""
Project : 사용자 정의 모듈 “MyMatrix.py” 을 준비하고, 행렬의 덧셈, 뺄셈, 곱셈 연산을 수행하는 함수/메소드
mtrxAdd(A, B), mtrxSub(A, B), mtrxMul(A, B), printMtrx(M)를 포함시켜라. 이 사용자 정의 모듈을 사용
자 정의 패키지 “MyPyPackage.myModules ”에 포함시킬 것. 다음 응용 프로그램을 사용하여 정확한 동
작을 확인할 것. 
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""

import random, time, sys
myPyPackage_dir = "G:/파이썬 특강/"
sys.path.append(myPyPackage_dir)
from MyPyPackage.myModules import MyMatrix

A = [[1,2,3,4], [5,6,7,8], [9,10,0,1]]
B = [[1,0,0,0], [0,1,0,0], [0,0,1,1]]
C = [[1,0,0], [0,1,0], [0,0,1], [0,0,0]]
print("A = "); MyMatrix.printMtrx(A)
print("B = "); MyMatrix.printMtrx(B)

D = MyMatrix.mtrxAdd(A, B)
print("A + B = "); MyMatrix.printMtrx(D)

E = MyMatrix.mtrxSub(A, B)
print("A - B = "); MyMatrix.printMtrx(E)

F = MyMatrix.mtrxMul(A, C)
print("A * C = "); MyMatrix.printMtrx(F)