"""
Project :  튜플을 사용한 학생 정보 처리
튜플 (학생이름, 학번, 학과명, 평균성적)로 표현되는 학생 (Student)의 정보를 10개 준비하여 학생 튜플 리스트 (list
of student-tuples)를 생성하라. 이 학생 튜플을 오름차순으로 정렬 (별도의 정렬 기준 설정 없이)하고, 결과를 출력하
라. 다음으로 학생튜플을 학점을 기준으로 역순으로 정렬하여 출력하라. 
Author: Chang‐Hyeop LEE
Date of last update: Jan. 5, 2022
"""
Student_data = ("Kim, S.C.", 12001234, "CE", 4.10), ("Choi, Y.B.", 119003234, "EE", 3.78), ("Hong, C.H.", 21001547, "ICE", 4.13), ("Yoon, J.H.", 17002571, "ME", 3.55),\
    ("Lee, S.H.", 20003257, "ICE", 4.45),("Kim, H.Y.", 19001234, "CE", 4.17),("Lee, J.K.", 18003234, "EE", 3.78),("Park, S.Y.", 21001643, "ICE", 4.13),\
    ("Jang, S.H.", 19002567, "ME", 3.35),("Yeo, C.S.", 20005243, "CE", 4.45)

for i in range(len(Student_data)):
    (name, st_id, major, GPA) = Student_data[i]
    print("students[{:2}] : name ({:>10}), st_id({:9}), major({:3} , GPA({:5.2f}))".format(i ,name, st_id, major, GPA))

none_standard_sorted = sorted(Student_data) # 별도의 정렬 기준 설정 없이 정렬
print()
print("After sorting in increasing oreder : ")
for i in range(len(Student_data)):
    (name, st_id, major, GPA) = none_standard_sorted[i]
    print("students[{:2}] : name ({:>10}), st_id({:9}), major({:3} , GPA({:5.2f}))".format(i ,name, st_id, major, GPA))

sorted_students = sorted(Student_data, key=lambda student: student[3], reverse = True) #GPA를 기준으로 정렬,  내림차순 정렬
print()
print("After sorting according to GPA in decreasing oreder : ")
for i in range(len(Student_data)):
    (name, st_id, major, GPA) = sorted_students[i]
    print("students[{:2}] : name ({:>10}), st_id({:9}), major({:3} , GPA({:5.2f}))".format(i ,name, st_id, major, GPA))