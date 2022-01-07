"""
Project : 중복되지 않는 정수형 난수의 리스트 생성, 샘플 출력 및 뒤섞기 기능을 제공하는 genRandList(L, size), printListSample(L,
per_line, sample_lines) 및 shuffleList(L)를 포함하는 사용자 정의 모듈
용 프로그램을 사용하여 정확한 동작을 확인할 것. 
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""

import random

def genRandList(L,size):
    for i in range(size):
        L.append(i)
    random.shuffle(L)
    

def printListSample(L, per_line, sample_lines):
    count = 0
    size = len(L) 
    for i in range(0, sample_lines): 
        s = ""
        for j in range(0, per_line): 
            if count > size:
                break
            s += "{0:>7} ".format(L[count]) 
            count += 1
        print(s) 
        if count >= size:
            break
    if count < size:
        print('. . . . . .') 
        if count < (size - per_line * sample_lines): 
            count = size - per_line * sample_lines 
        for i in range(0, sample_lines): 
            s = ""
            for j in range(0, per_line): 
                if count >= size:
                    break
                s += "{0:>7} ".format(L[count]) 
                count += 1
            print(s) 
            if count >= size:
                break

def shuffleList(L):
    random.shuffle(L)