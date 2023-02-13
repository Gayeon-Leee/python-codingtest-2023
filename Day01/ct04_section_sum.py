import sys
input = sys.stdin.readline # 입력 속도 개선 위한 부분,, 이 부분 없으면 백준 시관초과

N, M = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
sums = [0] # 핵심! 배열 0번째 인덱스를 채워놓고 시작하는거
temp = 0

for i in numbers:
    temp = temp + i # temp 5 9 12 14 15
    sums.append(temp)


for i in range(M):
    x, y = tuple(map(int, input().split()))
    print(sums[y] - sums[x - 1])