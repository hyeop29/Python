"""
Project : 튜플 (hour, min, sec)로 표현되는 시간 (time)을 표준 입력 장치로 부터 10개 입력하여 시간 튜플 리스
트 (list of time-tuples)에 포함시킨 후, 이 시간들을 오름 차순으로 정렬하는 파이썬 프로그램을 작성하
라. 입력 시간은 무작위로 설정할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 5, 2022
"""
TARGET_NUM_DATA = 10 # 입력 받을 data 수
num_data = 0
L_times = []

print("Input {} times in (hour minute sec) format :".format(TARGET_NUM_DATA))

while num_data < TARGET_NUM_DATA:
    (hour, minute, sec)=tuple(map(int,input("input hour minute second : ").split())) # 공백을 기준으로 입력 받은 후 int형으로 형변환 후 tuple로 생성
    L_times.append((hour, minute, sec)) #List에 튜플 추가
    print(L_times)
    num_data += 1

print("After input of 10 times : ")
print("L_times = {} ".format(L_times))
print("After sorting, L_dates = {} ".format(sorted(L_times))) # 리스트 정렬