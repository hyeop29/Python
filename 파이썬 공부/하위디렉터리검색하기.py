"""
특정 디렉터리부터 시작해서 그 하위 모든 파일 중 
파이썬 파일(*.py)만 출력해 주는 프로그램을 만들려면 어떻게 해야 할까 ?
"""
import os

def search(dirname) :
    try :
        filenames = os.listdir(dirname)
        for filename in filenames :
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename) :
                search(full_filename)
            else :
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py" :
                    print(full_filename)
    except PermissionError :
        pass

search("E:/")