def GuGu(X):
    answer = []
    for i in range(1, 10) :
        k = int(X) * i
        answer.append(k)

    return answer

X = input("숫자를 입력하세요 : ")
print(GuGu(X))