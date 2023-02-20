# 백준 10989번 문제 - 수 정렬하기3 => 정렬 문제 나오면 이 방법으로 푸는게 제일 나을 듯
import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for i in range(N):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)