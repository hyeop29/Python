def solution(left, right) :
    list_divisor = []
    answer = 0
    for i in range(left, right + 1) :
        for j in range(1, i + 1) :
            if i % j == 0 :
                list_divisor.append(j)
        if (len(list_divisor) % 2 == 0) :
            answer += max(list_divisor)
        else :
            answer -= max(list_divisor)
        list_divisor = []
    return answer

print(solution(13,17))