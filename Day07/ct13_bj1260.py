# 백준 1260번 문제 - DFS와 BFS
from queue import Queue
N, M, Start = map(int, input().split())
A = [[] for _ in range(N + 1)]  # 인접리스트

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)  # 무방향 엣지라 양쪽에 노드 추가

for i in range(N+1):
    A[i].sort() # 번호가 작은 노드부터 탐색(방문)해야하기 때문에 정렬

visited = []    # 리스트 변수 선언

# DFS함수 정의
def DFS(v):
    print(v, end=' ')
    visited[v] = True   # 방문
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# BFS함수 정의
def BFS(v):
    q = Queue()
    q.put(v)
    visited[v] = True
    while q.empty() != True :
        now = q.get()
        print(now, end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                q.put(i)

# DFS 실행
visited = [False] * (N + 1) # 초기화
DFS(Start)
print()
# BFS 실행
visited = [False] * (N + 1) # 초기화
BFS(Start)
print()