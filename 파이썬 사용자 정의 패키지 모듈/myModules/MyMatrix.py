"""
Project :행렬의 덧셈, 뺄셈, 곱셈 연산을 수행하는 함수/메소드
mtrxAdd(A, B), mtrxSub(A, B), mtrxMul(A, B), printMtrx(M)을 포함하는 사용자 정의 모듈
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""

def printMtrx(M):
    for i in range (len(M)):
        for j in range (len(M[i])):
            print("{:3}".format(M[i][j]),end = "")
        print()

def mtrxAdd(A,B):
    if (len(A) == len(B)) and (len(A[0]) == len(B[0])):   
        C = []
        for i in range (len(A)):
            temp=[]
            for j in range (len(A[0])):
                temp.append(A[i][j] + B[i][j])
            C.append(temp)
    else :                                       # 두 행렬의 크기가 다르면 덧셈 불가능
        print("두 행렬은 더 할 수 없습니다.") 

    return C

def mtrxSub(A,B):
    if (len(A) == len(B)) and (len(A[0]) == len(B[0])):
        C = []
        for i in range (len(A)):
            temp=[]
            for j in range (len(A[0])):
                temp.append(A[i][j] - B[i][j])
            C.append(temp)
    else :                                       # 두 행렬의 크기가 다르면 덧셈 불가능
        print("두 행렬은 뺄 수 없습니다.") 

    return C

def mtrxMul(A,B):
    if (len(A[0]) == len(B)):
        C = []
        for i in range (len(A)):
            temp_lsit=[]
            for j in range (len(B[0])):
                temp = 0
                for k in range (len(B)):
                    temp += A[i][k] * B[k][j]
                temp_lsit.append(temp)
            C.append(temp_lsit)
    else :                                       # 두 행렬 중 한 행렬의 열과 다른 행렬의 행의 크기가 다르면 곱셈 불가능
        print("두 행렬은 곱할 수 없습니다.") 

    return C