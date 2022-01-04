"""
Project : 3개의 16진수 x, y, z를 각각 입력 받고, 이 16진수 x와 y의 bit-wise and, bit-wise or, bit-wise
exclusive or 값을 각각 계산하여 2진수 및 16진수로 출력하며, x의 bit-wise not과 bit-wise left
shift 2, y와 z의 bitwise right shift 2를 각각 출력하는 파이썬 프로그램을 작성하고, 실행 결과
를 제출하라. 각 출력 항목들은 오른쪽으로 줄 맞춤 할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""

x = int(input("hexadecimal x = "),16)    #16진수 입력 받기
y = int(input("hexadecimal y = "),16)
z = int(input("hexadecimal z = "),16)

print("x = {:#4d} in decimal, {:#16b} in bits".format(x, x))  #10진수와 2진수 형태로 출력
print("y = {:#4d} in decimal, {:#16b} in bits".format(y, y))
print("z = {:#4d} in decimal, {:#16b} in bits".format(z, z))

print("x & y = in hex({:#6x}), in bin({:#16b})".format(x&y,x&y)) #bit 연산 결과 출력
print("x | y = in hex({:#6x}), in bin({:#16b})".format(x|y,x|y))
print("x ^ y = in hex({:#6x}), in bin({:#16b})".format(x^y,x^y))
print("x & y = in hex({:#6x}), in bin({:#16b})".format(x&y,x&y))
print("~x    = in hex({:#6x}), in bin({:#16b})".format(~x,~x))
print("x << 2 = in hex({:#6x}), in bin({:#16b})".format(x<<2,x<<2))
print("y >> 2 = in hex({:#6x}), in bin({:#16b})".format(y>>2,y>>2))
print("z >> 2 = in hex({:#6x}), in bin({:#16b})".format(z>>2,z>>2))