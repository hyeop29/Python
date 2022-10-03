b = '12123425125'
print(b[::-2])


number = 10
day = 'three'
a = "I ate %d apples. so I was sick for %s days. " %(number, day)
print(a)


a = "나의 이름은 {}". format("이창협")
print(a)


a= "hobby"
print(a.find('x')) 
# find 함수는 있으면 해당 위치 반환, 없으면 -1 반환
# index 함수도 있는데 있으면 해당 위치 반환, 없으면 오류

a = ",".join("abcd")
print(a)

a = "       hi"
print(a.strip())
# strip은 공백을 제거하는 함수

a = "Life is too short"
print(a.replace("Life", "Your leg"))
# Life 라는 단어를 Your leg로 대체

print(a.split())
# 띄어쓰기 기준으로 잘라서 리스트를 만든다. () 안에 값으로 특정한 기준으로 나눌 수 있다.

# 리스트 []
# 리스트 = 변수 여러 개를 묶는 역할
# 리스트 안에 리스트를 넣을 수도 있다.

# 튜플 ()
# 튜플은 리스트와 다르게 추가 할 수 없다. 튜플은 고정되어 있다.

# 딕셔너리 {} 
dic = {'name' : 'Eric', 'age' : 15}
print(dic.get('name','없음'))


a = 1
b = a
a = 3
print(id(a))
print(id(b))
