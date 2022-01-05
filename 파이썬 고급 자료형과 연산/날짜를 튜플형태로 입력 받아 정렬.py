"""
Project : 튜플 (year, month, day)로 표현되는 날짜 (date)을 표준 입력장치로 부터 10개 입력하여 날짜 튜플 리
스트 (list of date-tuples)에 포함시킨 후, 이 날짜들을 오름차순으로 정렬하는 파이썬 프로그램을 작성
하라. 입력 날짜는 무작위로 설정할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 5, 2022
"""
TARGET_NUM_DATA = 10 # 입력 받을 data 수
num_data = 0
L_dates = []

print("Input {} dates in (year month day) format :".format(TARGET_NUM_DATA))

while num_data < TARGET_NUM_DATA:
    (year, month, day)=tuple(map(int,input("input years, month, day : ").split())) # 공백을 기준으로 입력 받은 후 int형으로 형변환 후 tuple로 생성
    L_dates.append((year, month, day)) #List에 튜플 추가
    print(L_dates)
    num_data += 1

print("After input of 10 dates : ")
print("L_dates = {} ".format(L_dates))
print("After sorting, L_dates = {} ".format(sorted(L_dates))) # 리스트 정렬