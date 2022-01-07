"""
Project : 사용자 정의 패키지/서브패키지 “C:/MyPyPackage/myModules/” 에 선택 정렬 알고리즘을 구현한
selectionSort(L)을 포함하는 사용자 정의 “MySortings.py”을 구현하라. 앞에서 구현한 사용자 정의 모듈
“MyList.py”을 함께 사용하는 다음 응용 프로그램을 사용하여 정확한 동작을 확인하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""
import sys
myPyPackage_dir = "G:/파이썬 특강/"
sys.path.append(myPyPackage_dir)

from MyPyPackage.myModules import MyList, Mysortings

L = []
n = 100

MyList.genRandList(L, n)
print("Before Sorting :")
MyList.printListSample(L, 10, 3)

Mysortings.selectionSort(L)

print("\nAfter Sorting :")
MyList.printListSample(L, 10, 3)