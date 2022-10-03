score = 70

if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
print("-------------------------------------")
# 위와 같은 코드
message = "success" if score >= 60 else "failure"
print(message)
print("-------------------------------------")

# 반복문과 조건문에서 0이면 false 1이면 true 이다.
 
 # * 을 쓰면 함수에 여러 개의 변수를 입력값으로 쓸 수 있다.
def sum_many(*args):
    sum = 0
    for i in args :
        sum = sum + i
    return sum
print(sum_many(1,2,3,4,5))
print("-------------------------------------")

# **을 쓰면 dictionary 형태의 변수를 함수 입력값으로 쓸 수 있다.
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if( k == "name"):
            print("당신의 이름은 : " + kwargs[k])
print(print_kwargs(a="1", b="2", name="창협"))
print("-------------------------------------")

def add(a,b):
    return a + b
print(add(1,2))
print("-------------------------------------")
# 위 code 를 lambda를 사용해서 만들 수 있다.
add = lambda a, b: a+b
print(add(1,2))
print("-------------------------------------")
myList = [lambda a, b: a+b, lambda a, b: a*b]
print(myList[0](2,2))
print("-------------------------------------")
# input 함수 사용해보기
number = input("숫자를 입력하세요: ")
print(number)
print("-------------------------------------")

# 파일 쓰기
f = open("newFile.txt", 'w')
f.close()

# encoding 값을 UTF-8 으로 설정해주면 VS CODE TOOL 에서 한글이 깨지지 않는다.
f = open("newFile.txt", 'w',encoding="UTF-8")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파일 읽기
# txt 파일 한 줄 읽기
f = open("newFile.txt", 'r', encoding="UTF-8")
line = f.readline()
print(line)
f.close()

print("-------------------------------------")

# 여러 줄 읽기
f = open("newFile.txt", 'r', encoding='UTF-8')
while True:
    line = f.readline()
    if not line :
        break
    print(line)
f.close()

print("-------------------------------------")

# readlines() 함수 사용
f = open("newFile.txt", 'r', encoding='UTF-8')
lines = f.readlines() # readlines 함수를 통해 파일에 있는 모든 라인들을 읽어온다.
for line in lines:
    print(line, end = "")  # print(line.strip("\n")) 과 같은 기능이다.
f.close()

print("-------------------------------------")

# read() 함수 사용
f = open("newFile.txt", 'r', encoding='UTF-8')
data = f.read()
print(data)
f.close()

# 추가 모드 사용 , 'w' 와 'a'의 차이는 w는 기존 파일의 값을 다 지우고 새로 작성
# a는 기존 파일의 값 뒤에서부터 작성한다.
f = open("newFile.txt", 'a', encoding='UTF-8')
for i in range(11,20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 파이썬 개념
# 변화지 않는 자료형 : 정수, 실수, 문자열, 튜플
# 변할 수 있는 자료형 : 리스트, 딕셔너리, 집합
# 아래 예제 참고
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

print("-------------------------------------")

b = [1,2,3]
def vartest2(b):
    b = b.append(4)
vartest2(b)
print(b)