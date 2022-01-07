"""
Project : 선택 정렬 알고리즘을 구현한 selectionSort(L), 병합정렬 (mergeSort) 기능을 수행하는 함수/
메소드 mergeSort(L)을 포함하는 사용자 정의 모듈
Author: Chang‐Hyeop LEE
Date of last update: Jan. 7, 2022
"""

#선택 정렬
def selectionSort(L):
    size = len(L)
    for i in range(0, size-1):
        min_idx = i
        for j in range(i+1, size):
            if (L[min_idx] > L[j]):
                min_idx = j
        if (min_idx != i):
            L[min_idx], L[i] = L[i], L[min_idx]

#병합 정렬
def _merge(L_left, L_right):
    L_res = []
    i, j = 0, 0
    len_left, len_right = len(L_left), len(L_right)
    while i < len_left and j < len_right:
        if L_left[i] < L_right[j]:
            L_res.append(L_left[i])
            i += 1
        else:
            L_res.append(L_right[j])
            j += 1
    while (i < len_left):
        L_res.append(L_left[i])
        i += 1
    while (j < len_right):
        L_res.append(L_right[j])
        j += 1
    return L_res

def mergeSort(L): # merge_sort in increasing order
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        L_left = mergeSort(L[:middle])
        L_right = mergeSort(L[middle:])
        return _merge(L_left, L_right)