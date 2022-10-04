# 필요한 기능 - 문서 파일 읽어 들이기, 문자열 변경하기
# 입력 받는 값 - 탭을 포함한 문서 파일
# 출력하는 값 - 탭이 공백으로 수정된 문서 파일
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t"," "*4) # 탭을 공백 4칸으로 replace

f = open(dst, 'w')
f.write(space_content)
f.close()
