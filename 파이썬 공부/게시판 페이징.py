total, page = map(int, input("게시물 총 건수와 한 페이지에 보여줄 게시물 수를 입력하세요 : ").split())

def page_num(total,page) :
    if total % page == 0 :
        return total // page
    else :
        return total // page + 1
result = page_num(total, page)

print("총 페이지 수는 {} 입니다.".format(result))
