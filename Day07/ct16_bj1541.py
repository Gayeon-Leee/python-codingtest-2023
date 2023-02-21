# 백준 1541번 문제 - 잃어버린 괄호
answer = 0
A = list(map(str, input().split('-')))  # - 기준으로 잘라서 문자열로 리스트 

def mySum(i):
    result = 0
    temp = str(i).split('+')    # + 기준으로 수식 자름

    for k in temp:
        result += int(k)    # 문자열 리스트이기때문에 int로 형변환

    return result

for s in range(len(A)):
    temp = mySum(A[s])

    if s == 0:
        answer += temp  # 맨 처음
    else:
        answer -= temp

print(answer)