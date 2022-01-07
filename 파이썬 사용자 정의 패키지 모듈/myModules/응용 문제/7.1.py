"""
Project : 사용자 정의 패키지/서브패키지 “C:/MyPyPackage/myModules/”를 생성하고, 중복되지 않는 정수형 난
수의 리스트 생성, 샘플 출력 및 뒤섞기 기능을 제공하는 genRandList(L, size), printListSample(L,
per_line, sample_lines) 및 shuffleList(L)를 포함하는 사용자 정의 모듈 “MyList.py”을 준비하라. 다음 응
용 프로그램을 사용하여 정확한 동작을 확인할 것. 
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""

import sys
myPyPackage_dir = "G:/파이썬 특강/"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList

L = []
n = 100

MyList.genRandList(L, n)
MyList.printListSample(L, 10, 5)