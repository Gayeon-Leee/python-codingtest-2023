# 백준 1253번 문제 - 좋다(GOOD)

import sys
input = sys.stdin.readline

N = int(input())
count = 0
A = list(map(int, input().split())) # 입력을 한 줄에 여러개 받으려고 split 써서 받는것
A.sort()    # sort(reverse = True)는 역순정렬 ** 디버깅할 때 이 줄에 중단점

for k in range(N):
    find = A[k]
    i = 0; j = N - 1    # i는 리스트 첫번째 , j는 리스트 마지막에 위치
    while i < j:    # 두 인덱스가 만나면 while문 종료
        if A[i] + A[j] == find: # 두 수의 합이 찾는 수랑 일치
            if i != k and j != k:   #i,j는 k와 같은 위치가 되면안됨
                count += 1
                break
            elif i == k: i += 1
            elif j == k: j -= 1
        elif A[i] + A[j] < find:    # i를 증가시켜야 합산된 수가 커짐 
            i += 1
        elif A[i] + A[j] > find:    #j 감소시키면 합산값 작아짐
            j -= 1

print(count)