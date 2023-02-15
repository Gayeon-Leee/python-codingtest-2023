# 큐 구현
# 전역변수
SIZE = 0
queue = []
front = rear = -1

# Queue Full 확인
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE -1):
        return False
    elif (rear == SIZE -1) and (front == -1):
        return True
    else:   #deQueue를 한 뒤 뒤의 데이터를 당겨와 빈자리를 채우는 것 => 없으면 앞의 데이터 빼고나서 None 으로 남음
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1   # 1씩 감소
        return False

    #단순 full 확인
    # if (rear == SIZE -1):
    #     return True
    # else:
    #     return False
    

# Queue Empty 확인
def isQueueEmpty(): 
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return False

# Queue 데이터 추가    
def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full')
    else:
        rear += 1
        queue[rear] = data

# Queue 데이터 삭제 - 어차피 순서대로 빠지기때문에 빠질 데이터 지정 X
def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else:   #deQueue를 한 뒤 뒤의 데이터를 당겨와 빈자리를 채우는 것 => 없으면 앞의 데이터 빼고나서 None 으로 남음
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1   # 1씩 감소
        return data
    
# Queue front+1 위치값 확인
def peek():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is Empty')
        return None
    else:
        return queue[front+1]
    

# 메인 엔트리
if __name__ == '__main__':
    SIZE = int(input('큐 사이즈 입력 >> '))
    queue = [None for _ in range(SIZE)] # SIZE 처럼 변수를 대문자로 쓰면 원래는 상수로 사용.. 값을 바꾸지 않음

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) >> ')
        if select.lower() == 'x':
            break
        elif select.lower() == 'i':
            data = input('입력데이터 >>')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'e':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'v':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')

        else:
            continue

    print('큐 프로그램 종료')