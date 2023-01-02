"""
Project : 
위 문제 5.1에서 구현한 class Person을 상속받는 class Student를 구
현하라. class Student는 추가적인 속성으로 정수형의 학번 (student_id), 
문자열의 전공명 (major), 실수형 (float)의 평균성적 (GPA)를 가진다. 
class Student의 생성자 (initiator) 및 student_id, major, GPA의 접근자
(accessor)와 변경자 (mutator)를 구현하라. 변경자에서는 데이터 멤버의
값이 설정/변경될 때 정상적인 범위의 값으로 설정/변경되는지 확인하는
기능을 포함하도록 하고, 생성자 __init__() 함수에서는 각 데이터 멤버의
변경자를 사용하여 초기값 설정을 하도록 하라.
class Student 객체에 대하여 print() 함수로 출력할 때 사용되는 문자열을
제공하기 위한 __str__() 함수로 구현하라. 
10명의 학생 정보를 class Student로 생성하여 리스트에 포함시키고, 이
학생들을 이름 순, 학번 순, 성적 순으로 정렬하여 출력하는 시험 프로그
램을 if __name__ == “__main__” 조건을 사용하여 실행하도록 구현하고, 
실행 결과를 확인하라.
Author: Chang‐Hyeop LEE
Date of last update: Jan. 2, 2022
"""
from Homework5_1 import Person

class Student(Person) :
    def __init__(self, name, age, st_id, major, gpa) :
        Person.__init__(self, name, age)
        self.setSTID(st_id)
        self.setMajor(major)
        self.setGPA(gpa)
    def getSTID(self):
        return self.st_id
    def getMajor(self):
        return self.major
    def getGPA(self):
        return self.gpa
    def setSTID(self, st_id):
        self.st_id = st_id
    def setMajor(self, major):
        major_list = ["EE", "ICE", "ME", "CE"]
        if major in major_list :
            self.major = major
        else :
            print("Error in setting major (name: {}, age:{})".format(self.name, major))
            self.major = None
    def setGPA(self, gpa):
        self.gpa = gpa
    def __str__(self):
        return "Student({}, {}, {}, {}, {})".format(self.getName(), self.getAge(), self.getSTID(), self.getMajor(), self.getGPA())

def printStudents(students) :
    for i in students :
        print(i)

def sortStudent(students, type) :
    if type == "name" :
        students.sort(key=lambda x: x.name)
    elif type == "st_id" :
         students.sort(key=lambda x: x.st_id)
    elif type == "GPA" :
         students.sort(key=lambda x: x.gpa, reverse = True)

if __name__ == "__main__":
    students = [
    Student("Kim", 21, 12345, "EE", 4.0),
    Student("Lee", 22, 11234, "ME", 4.2),
    Student("Park", 20, 10234, "ICE", 4.3),
    Student("Hong", 19, 13123, "CE", 4.1),
    Student("Yoon", 23, 11321, "ICE", 4.2)
    ]
    print("students before sorting : ")
    printStudents(students)
    
    sortStudent(students, "name")
    print("₩nstudents after sorting by name : ")
    printStudents(students)
    
    sortStudent(students, "st_id")
    print("₩nstudents after sorting by student_id : ")
    printStudents(students)
    
    sortStudent(students, "GPA")
    print("₩nstudents after sorting by GPA in decreasing order: ")
    printStudents(students)
