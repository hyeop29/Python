def sum_3_5(n):
    i = 1
    answer = []
    for i in range(1,n) :
        if (i % 3  == 0) or (i % 5 == 0) :
            answer.append(i)
    result = sum(answer)
    return result 


while(1) :
    n = int(input("1000미만 숫자를 입력하세요 : "))
    if n >= 1000 :
        continue
    else :
        print(sum_3_5(n))
        break
