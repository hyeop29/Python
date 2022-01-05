"""
Project : ASCII 문자표에서 영문 대문자, 소문자, 숫자를 리스트 (list)로 구성하고 출력하는 파이썬 프로그램을
작성하라. 
Author: Chang‐Hyeop LEE
Date of last update: Jan. 5, 2022
"""
Upper_alphabets = list(range(0x41,0x5B))  #리스트 3개 준비
Lower_alphabets = list(range(0x61,0x7B))
Digists = list(range(0x00,0x0A))

Upper_alphabets_chr = list(map(chr,Upper_alphabets)) #Upper_alphabets list를 chr로 바꾼 뒤 list로 만들어준다
Lower_alphabets_chr = list(map(chr,Lower_alphabets))
Digists_int = list(map(int,Digists)) #Digists list를 int로 바꾼 뒤 list로 만들어준다

#각 각 리스트 출력
print("Upper case alphabets : ")
print(Upper_alphabets_chr)

print("Lower case alphabets : ")
print(Lower_alphabets_chr)

print("Digits : ")
print(Digists_int)