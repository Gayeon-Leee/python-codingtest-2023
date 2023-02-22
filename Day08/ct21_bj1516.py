# 백준 1516번 문제 - 게임개발
from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]    # 0번 인덱스 사용 안한다는 것
indegree = [0] * (N + 1)  # 진입차수
selfBuild = [0] * (N + 1)   # 자기 건물 빌드 시간

for i in range(1, N+1):
    inputList = list(map(int, input().split())) 
    selfBuild[i] = inputList[0] # 건물 빌드 시간
    index = 1
    while True: # 인접리스트
        preTemp = inputList[index]
        index += 1
        if preTemp == -1: break # while문 탈출

        A[preTemp].append(i)
        indegree[i] += 1    # 진입차수 증가

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i) # 1부터 시작

result = [0] * (N+1)

while q:    #위상정렬 수행
    now = q.popleft()
    for next in A[now]:
        indegree[next] -=1   #방문했으니까 1 감소
        # 시간 업데이트
        result[next] = max(result[next], result[now] + selfBuild[now])
        if indegree[next] == 0:
            q.append(next)

for i in range(1, N+1):
    print(result[i] + selfBuild[i])