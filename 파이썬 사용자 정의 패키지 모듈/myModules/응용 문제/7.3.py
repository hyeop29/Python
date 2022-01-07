"""
Project : 앞의 Homework 7.1과 7.2에서 준비한 사용자 정의 모듈 MyList와 MySortings을 사용하여 중복되지 않
는 50000개의 정수형 난수를 포함하는 리스트를 생성하라. 아울러, 파이썬 기본 제공 모듈인 array를 사
용하여 정수형 난수 리스트에 포함된 원소들을 배열에 포함시켜라. 다음 응용 프로그램을 사용하여 리
스트와 배열에 포함된 난수들을 선택 정렬시키고, 실행시간을 측정하여 비교하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""
import random, time, sys
from array import *
sys.path.append("G:/파이썬 특강/")
from MyPyPackage.myModules import MyList, Mysortings

AR = array('i')
L = []
size = 50000
L = MyList.genRandList(L, size)

for x in L:
    AR.append(x)

print("Array (size : {}) before sorting : ".format(size))
MyList.printListSample(AR, 10, 2)
t1 = time.time()
Mysortings.selectionSort(AR)
t2 = time.time()
print("Array (size : {}) after sorting : ".format(size))
MyList.printListSample(AR, 10, 2)
print("Selection sorting for array of {} integers took {} sec"\
.format(size, t2-t1))

print("\nList (size : {}) before sorting : ".format(size))
MyList.printListSample(L, 10, 2)
t1 = time.time()
Mysortings.selectionSort(L)
t2 = time.time()
print("\nList (size : {}) after sorting : ".format(size))
MyList.printListSample(L, 10, 2)
print("Selection sorting for list of {} integers took {} sec"\
.format(size, t2-t1))