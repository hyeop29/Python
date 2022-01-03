"""
Project : 10개의 실수 (float) 데이터를 차례로 입력받고, 입력된 데이터의 최댓값, 최솟값, 평균값를 계산하여 출
력하는 파이썬 프로그램을 작성하고, 실행 결과를 제출하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 3, 2022
"""
TARGET_NUM_DATA = 10
num_data = 0
L_data = [] #empty list
L_sum = 0

while num_data < TARGET_NUM_DATA:
    data = float(input("input %d-th float data = " % num_data)) # 입력된 문자열을 float으로 사용하기 위해 float으로 바꾼다
    L_data.append(data)
    L_sum = L_sum + data
    num_data += 1
    if num_data == 1:
        min = max = data
    if min > data:
        min = data # min
    if max < data:
        max = data # max
    
avg = L_sum / num_data # avg

print("Input data = " , L_data)
print("min = {}, max = {}, avg = {}".format(min, max, avg))

