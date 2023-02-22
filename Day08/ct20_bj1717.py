# 백준 1717번 문제 - 집합의 표현
# Union-Find 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
N, M = map(int, input().split())
parent = [0] * (N + 1)  # [0 for  _ in range(N+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[0]) # 재귀호출 -> 경로압축

def union(a, b):    # 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a, b):    # 둘이 같은 집합인지
    a = find(a)
    b = find(b)

    if a == b: return True
    else: return False

for i in range(0, N + 1):
    parent[i] = i # 1-1 , 2-2, 3-3, 4-4, 5-5 이렇게 들어가도록 초기화

for i in range(M):
    question, a, b = map(int, input().split())  # 0 1 3 or 1 1 7
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print('YES')
        else:
            print('No')