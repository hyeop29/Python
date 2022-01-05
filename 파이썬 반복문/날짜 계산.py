"""
Project : 날짜를 나타내는 연(year), 월(month), 일(day)의 3개 정수를 입력 받고, 이 날이 서기 1년 1월 1일부터
몇 번째 날짜인지를 계산하며, 이 날이 무슨 요일인지 계산하여 출력하는 파이썬 프로그램을 작성하라.
참고로 서기 1년 1월 1일은 월요일이다. 프로그램은 0 0 0이 입력될 때 까지 반복하도록 할 것.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 4, 2022
"""
L = [0, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
D = ["SUN", "MON", "TUE", "WEN", "THR", "FRI", "SAT"]
while True:
    year, month, day = map(int, input("input year month day: ").split())
    elsaped = 0
    count = 0

    if((year == 0) and (month == 0) and (day == 0)): # 0 0 0 입력 받으면 종료
        break
    elif(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
        L[2] = 29
        print(D)

    for i in range (1,year):
        year_days = 365
        if(((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0)):
             year_days = 366
        elsaped += year_days

    elsaped += sum(L[:month])
    elsaped += day

    week_day= elsaped % 7

    print("Day (year({}), month({}), day({})) : week_day ({}), elapsed {} days from Jan01AD01".format(year, month, day, D[week_day], elsaped))
 