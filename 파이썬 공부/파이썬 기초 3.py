# 클래스 : 반복되는 변수 & 메서드(함수)를 미리 정해놓은 틀(설계도)
# 클래스는 왜 필요한가 ?
# 두 개의 서로 다른 계산기가 필요하다고 가정하자.
from distutils.command.build_scripts import first_line_re


result1 = 0
result2 = 0

def add1(num) :
    global result1
    result1 += num
    return result1

def add2(num) :
    global result2
    result2 += num
    return result2
   
print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
# 똑같은 함수를 2번 써야하는 상황이 발생하기 때문에 class를 사용한다.
class Calculator :
    def __init__(self):
        self.result = 0
    
    def add(self, num) :
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print("-------------------------------------")
class FourCal:
    # init 함수는 클래스 처음 만들 때 무조건 가장 먼저 자동으로 수행
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)
print(a.add())

print("-------------------------------------")

# 클래스의 상속, 부모가 만든 건 자식이 다 쓸 수 있다.
# 자식이 부모의 함수 변형도 가능하다. => 매서드 오버라이딩
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.second == 0:
            return 0
        else :
            return self.first / self.second

b = MoreFourCal(4, 2)
b. add()

# 모듈 : 미리 만들어 놓은 .py 파일 (함수, 변수, 클래스)
# 모듈 main에서만 실행하게 하는 방법    if __name__ == "__main___" : 
# 다른 경로에 있는 모듈 가져다 쓰는 법
# import sys
# sys.path.append ("경로")

# 패키지 : 모듈 여러 개 모아놓은 것, 라이브러리와 비슷한 개념

# 예외처리 : 오류가 발생했을때 어떻게 할지 정하는 것
# 기본 구조
# try:
#   # 오류가 발생할 수 있는 구문
# except Exception as e:
#   # 오류 발생
# esle:
#   # 오류 발생하지 않음
# finally:
#   # 무조건 마지막에 실행
try :
    4 / 0
except ZeroDivisionError as e:
    print(e)

print("-------------------------------------")

try :
    f = open('none.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else :
    data = f.read()
    print(data)
    f.close()

# 내장함수 : 파이썬에서 기본적으로 포함하고 있는 함수 ex) print(), type() 
# 외장함수 : 라이브러리 함수, import 해서 쓰는 것

def positive(x):
    return x > 0

a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)