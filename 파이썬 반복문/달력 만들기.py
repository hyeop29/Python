"""
Project : 날짜를 나타내는 연(year), 월(month), 일(day)의 3개 정수를 입력 받고, 이 달의 달력을 출력하는 파이
썬 프로그램을 작성하라. 달력의 첫 줄은 요일을 의미하는 영문 약자 (SUN, MON, TUE, WED, THR, FRI,
SAT)를 출력하고, 이 달의 1일 부터 요일에 맞추어 출력되도록 할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""
L = [0, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
D = ["SUN", "MON", "TUE", "WEN", "THR", "FRI", "SAT"]
M = ["", "January", "February", " March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

year, month, day = map(int,(input("input year month day : ").split())) # 년, 월, 일 입력 받기

elsaped = 0
count = 0

for i in range (1,year):
    year_days = 365
    if(((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0)):
        year_days = 366
    elsaped += year_days

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    L[2] = 29

elsaped += sum(L[:month])
temp = elsaped % 7 + 1      #달력의 공백을 위한 연산
elsaped += day
week_day= elsaped % 7

print("{} of Year {}".format(M[month], year))
print("=============================")
print(" SUN MON TUE WED THR FRI SAT ")
print("-----------------------------")
for i in range (temp):
    count += 1
    print("    ",end='')
for i in range (1,L[month]+1):
    count += 1
    print("{:4d}".format(i),end='')
    if (count == 7):
        print()
        count = 0
print()
print("=============================")
    