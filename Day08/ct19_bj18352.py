# 백준 18352번 문제 - 특정거리 도시 찾기
import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())    # 노드 수, 에지 수 , 목표거리, 시작노드
A = [[] for _ in range(N+1)]    # 초기화
answer = [] # 값 담을 빈 리스트
visited = [-1] * (N+1)  # 방문리스트 초기화

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] += 1
    while q:
        now = q.popleft()
        for i in A[now]:
            if visited[i] == -1:    # 한 번도 방문 안했으면
                visited[i] = visited[now] + 1
                q.append(i)

# 두번째 줄 부터 에지 입력
for _ in range(M):
    s, e = map(int, input().split()) 
    A[s].append(e)               

BFS(X)  # 시작점부터 BFS 시작

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)