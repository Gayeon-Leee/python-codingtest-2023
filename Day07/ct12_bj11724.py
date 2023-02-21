# 백준 11724번 문제 - 연결요소 개수 확인
import sys
# 파이썬에 재귀호출 제한 있음 (1000번까지 가능) -> 제한 풀어줘야함
sys.setrecursionlimit(10 ** 6)  # 1000000번까지 가능하도록 제한 해제
input = sys.stdin.readline  # 입력 속도 빠르게 하는 것 =>  없으면 입력 속도가 느려서 백준에서 돌리면 입력 오류 발생 가능

n, m = map(int, input().split())    # 6 5
A = [[] for _ in range(n+1)]    # x행, 7열의 2차원 리스트
visited = [False] * (n + 1)  # 6 넣을 경우 [0, 1, 2, 3, 4, 5, 6] 생성, 0은 사용X

# DFS 함수
def DFS(v):
    visited[v] = True    # 원래 False 인 방문 노드를 True로
    for i in A[v]:
        if not visited[i]:   # 방문을 안했다면
            DFS(i)

for _ in range(m):   # 에지의 개수만큼 반복
    s, e = map(int, input().split())
    A[s].append(e)  
    A[e].append(s)  # 무방향이기 때문에 양쪽에 에지 추가해야 하는 것

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)