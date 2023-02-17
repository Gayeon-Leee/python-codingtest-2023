## C:\Windows\System32 파일 출력

import os

# print(dir(os)) os에 속한 기능 확인
def makeFileList(folder):
    fnameAry = []
    for _, _, fnames in os.walk(folder):
        for fname in fnames:
            fnameAry.append(fname)
    return fnameAry

def insertionSort(ary):
    n = len(ary)
    for end in range(1, n):  # 0번자리 값 빼고 1번자리 부터 끝가지 반복
        for cur in range(end, 0, -1):   # 위와 반대로
            if ary[cur-1] < ary[cur]: # 내림차순(역순 정렬)
                 ary[cur-1], ary[cur] = ary[cur], ary[cur-1]    # 파이썬에 있는 swap
              
    return ary

fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print('파일명 역순 출력 ->', fileAry)