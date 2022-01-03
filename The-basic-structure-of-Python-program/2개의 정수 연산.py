"""
Project : 2개의 정수 a와 b를 입력받아 정수연산 a+b, a-b, a*b, a/b, a//b, a%b를 각각 계산하여 출력하는 파이
썬 프로그램을 작성하고, 실행 결과를 제출하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 3, 2022
"""
a, b = map(int, input("input a and b : ").split()) # split은 입력받은 값을 공백을 기준으로 분리

print("a({}) + b({}) = {}" .format(a, b, a + b))
print("a({}) - b({}) = {}" .format(a, b, a - b))
print("a({}) * b({}) = {}" .format(a, b, a * b))
print("a({}) / b({}) = {:.6f}" .format(a, b, a / b))
print("a({}) // b({}) = {:.6f}" .format (a, b, a // b))
print("a({}) % b({}) = {:.6f}" .format(a, b, a % b))