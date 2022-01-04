"""
Project : 복소수 (complex number) c1을 입력 받고, 이 c1의 켤레 복소수 c2를 계산하여 출력하라. c1
과 c2의 덧셈, 뺄셈, 곱셈, 나눗셈을 계산하여 결과를 출력하는 파이썬 프로그램을 작성하고,
실행 결과를 제출하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""

c1 = complex(input("input c1 (in complex, re = imj): ")) #복소수 입력 받기
c2 = complex.conjugate(c1) #켤레 복소수

print("c1 = {}".format(c1))
print("c2 = conjugate of c1 = {}".format(c2))
print("c1 + c2 = {}".format(c1+c2)) #복소수 연산
print("c1 - c2 = {}".format(c1-c2))
print("c1 * c2 = {}".format(c1*c2))
print("c1 / c2 = {}".format(c1/c2))
