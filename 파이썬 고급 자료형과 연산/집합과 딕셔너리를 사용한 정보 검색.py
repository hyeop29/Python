"""
Project :  집합과 딕셔너리를 사용한 정보 검색
 총 10개의 국가에 대하여 문자열 (str) 자료형의 국가 이름과 수도 이름을 입력받고, 국가의 이름을 딕셔너리의
key로 사용하고, 그 국가의 수도의 이름 (문자열 자료형)을 value로 사용하는 딕셔너리 (dict_country_capital)를
구성하라.
 입력장치로 부터 국가 이름을 입력받아 해당 국가의 수도 이름을 찾아내는 파이썬 프로그램을 작성하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 5, 2022
"""
TARGET_NUM_DATA = 10 # 입력 받을 data 수
num_data = 0

dict_country_capital = {}

while num_data < TARGET_NUM_DATA:
    input_data_str =input("Input nation and its capital (. to quit) : ") 
    if input_data_str == '.':
        break
    key , value = input_data_str.split() # 공백을 기준으로 key 와 value 구분
    dict_country_capital[key] = value # 딕셔너리에 쌍 추가
    num_data += 1

print(dict_country_capital)

while True:
    key = input("Input nation to find its capital (. to quit) : ")
    if key == '.':
        break
    elif key in dict_country_capital:
        print("The captial of {} is {}".format(key,dict_country_capital[key]))
    else:                                                         # 찾고자하는 수도의 국가가 딕셔너리에 없을 경우
        print("Ther's no information about this {} ".format(key))