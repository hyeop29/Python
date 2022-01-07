# G:/MyPyPackage/myModules/MyFact.py
def fact_r(n):
    if n == 0:
        return 1
    return n * fact_r(n-1)
    
def fact_i(n):
    nFact = 1
    for i in range(n, 0, -1):
        nFact *= i
    return nFact