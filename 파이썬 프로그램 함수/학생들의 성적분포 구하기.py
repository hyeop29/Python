"""
Project : 학생 6명의 정보를 포함하는 튜플 (학생이름, 학과명, 학번, (연, 월, 일), 평균성적)들을 리스트에 포함시킨 후, 파이썬
내장함수 sum(), max(), min(), len()을 사용하여 학생들의 성적 분포 (최대, 최소, 평균)를 파악하여 출력하는 함수 statics_student_GPA()
함수를 구현하라.
Author: Chang‐Hyeop LEE
Date of last update: December. 29, 2022
"""
def statistics_student_GPA(L) :
    L_GPAs = []
    print("students = ")
    print(*L, sep= '\n')
    print("statics_student_GPA : ")

    for i in range(len(L)) :
        L_GPAs.append(L[i][4])

    print(" - L_GPAs = {}" .format(L_GPAs))
    print(" - num_students = {}" .format(len(L_GPAs)))
    print(" - Statistics of GPAs : MAX ({}), MIN ({}), AVG ({}) " .format(max(L_GPAs), min(L_GPAs), sum(L_GPAs)/len(L_GPAs)))


students = [('Kim', 'EE', 12345, (2000, 12, 25), 4.0)
            ,('Lee', 'ME', 11234, (2019, 9, 1), 4.2)
            ,('Park', 'ICE', 10234, (2019, 3, 1), 4.3)
            ,('Hong', 'CE', 13123, (2021, 1, 1), 4.1)
            ,('Yoon', 'ICE', 11321, (2001, 8, 15), 4.2)
            ,('A', 'ICE', 12321, (2000, 7, 31), 4.2)]

statistics_student_GPA(students)
