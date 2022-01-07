"""
Project : 앞에서 준비하였던 사용자 정의 모듈 “MySortings.py”에 병합정렬 (mergeSort) 기능을 수행하는 함수/
메소드 mergeSort(L)를 추가하라. 다음 응용 프로그램을 사용하여 50000개의 중복되지 않는 정수형 난
수에 대한 선택정렬과 병합정렬을 각각 실행시키고, 실행에 걸린 경과시간을 측정하여 비교하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""

import random, time, sys
sys.path.append("G:/파이썬 특강/")
from MyPyPackage.myModules import MyList, Mysortings

while True:
    size = int(input("\nsize of list (0 to terminate) = "))
    if size == 0:
        break

    L = []
    MyList.genRandList(L, size)
    print("List (size : {}) before merge sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    t1 = time.time()
    Mysortings.mergeSort(L)
    t2 = time.time()
    print("\nList (size : {}) after merge sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    print("Merge sorting for list of {} integers took {} sec".format(size, t2-t1))

    MyList.shuffleList(L)
    print("!!!!!!!!!!!!")
    print (L)
    print("\nList (size : {}) before selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    t1 = time.time()
    Mysortings.selectionSort(L)
    t2 = time.time()
    print("\nList (size : {}) after selection sorting : ".format(size))
    MyList.printListSample(L, 10, 2)
    print("Selection sorting for list of {} integers took {} sec".format(size, t2-t1))