# MyFact.py at G:/MyPyPackage/myModules/MyFact.py
import sys
sys.path.append("G:/MyPyPackage/myModules")
print("sys.path : ", sys.path)
from MyFact import *
while True:
    n = int(input('n for factorial(n) (‐1 to quit) : '))
    if n == -1:
        break
    print("fact_r({}) = {}".format(n, fact_r(n)))
    print("fact_i({}) = {}".format(n, fact_i(n)))