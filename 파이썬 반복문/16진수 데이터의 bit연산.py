"""
Project : 2개의 16진수 데이터 문자열을 한 줄로 입력 받고, 이를 정수로 변환하여 a와 b에 저장하라. 이 두 16진
수 a, b의 bit-wise AND, bit-wise OR, bit-wise XOR 값을 계산하여 출력하는 파이썬 프로그램을 작성하
라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""

strings = input("input two hexadecimal numbers (예: 0xA3 0x3A) : ").split() #문자열로 2개의 16진수 데이터 입력
a = int(strings[0],16) #문자열을 정수로 변환
b = int(strings[1],16)

print("a = {:#x} = {:#b}".format(a, a))
print("b = {:#x} = {:#b}".format(b, b))
print("a & b = {:#x} = {:#b}".format(a&b, a&b))
print("a | b = {:#x} = {:#b}".format(a|b, a|b))
print("a ^ b = {:#x} = {:#b}".format(a^b, a^b))