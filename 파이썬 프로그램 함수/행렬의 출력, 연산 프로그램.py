"""
Project : 행렬의 출력, 연산 프로그램
(1) 행렬을 표현하는 2차원 리스트 1개를 행렬의 이름 (문자열)과 함께 전달받아 출력하는 함수
printMtrx(name, M)을 작성하라. 
(2) 2차원 리스트 2개를 전달받아 행렬의 덧셈을 계산하여 결과를 반환하는 함수 matrixAdd(A, B), 
뺄셈을 계산하여 결과를 반환하는 함수 matrixSubtract(A, B), 그리고 곱셈을 계산하여 결과를 반
환하는 함수 matrixMultiply(A, B)를 작성하라. 
(3) 다음 기능 시험 프로그램을 사용하여 결과를 출력하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 1, 2022
"""
def printMtrx(name, M) :
    print("{} = ".format(name))
    for i in range(len(M)) :
        for j in range(len(M[i])) :
            print("{:3d}".format(M[i][j]), end = "")
        print("")
    print("")

def matrixAdd(A, B) :
    C = [[0 for col in range(len(A[0]))] for row in range(len(A))]
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrixSubtract(A, B) :
    C = [[0 for col in range(len(A[0]))] for row in range(len(A))]
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            C[i][j] = A[i][j] - B[i][j]
    return C

def matrixMultiply(A, B) :
    C = [[0 for col in range(len(A))] for row in range(len(B[0]))]
    for i in range(len(A)) :
        for k in range(len(B[0])) :
            for j in range(len(A[i])) :
                C[i][k] += A[i][j] * B[j][k]
    return C

A = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
B = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]]
printMtrx("A", A)
printMtrx("B", B)  
C = matrixAdd(A, B)
printMtrx("A+B", C)
D = matrixSubtract(A, B)
printMtrx("A-B", D)
E = matrixMultiply(A, B)
printMtrx("A*B", E)
