"""
Project : 10개의 실수 (float) 데이터를 한 줄에 입력 받아 리스트에 저장하고, 이 리스트에 포함된 데
이터 중 최솟값, 최댓값, 평균값을 계산하여 출력하라. 평균값은 소수점 이하 2자리까지 출력
할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 3, 2022
"""

TARGET_NUM_DATA = 10

float_strings = (input("input {} float data in one line (separated in space) = ".format(TARGET_NUM_DATA)).split()) 
L_float_data = list(map(float, float_strings)) #float_strings를 float 형식의 L_float_data list로 변경

print("float_strings = {}".format(float_strings))
print("L_float_data = {}".format(L_float_data))
print("L_max = ({}), L_min = ({}), L_avg = ({})".format(max(L_float_data), min(L_float_data), sum(L_float_data)/len(L_float_data)))