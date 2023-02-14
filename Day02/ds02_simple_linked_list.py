# 단순 연결리스트 구현
class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

#전역변수
memory = [] # == lists()
head, current, pre = None, None, None
dataArray = ['민혁', '기현', '형원', '주헌', '창균']

def printNodes(start):
    current = start
    if current == None:
        return   
    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data)
        else:
            print(current.data, end=' -> ')

# 노드 추가
def insertNode(findData, insertData):
    global memory, pre, current, head

    if head.data == findData:    # 맨 앞에 노드 추가
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head # current를 제일 앞으로 땡겨주는 것(위에서 print 돌고나면 맨 뒤로 가있음)
    while current.link != None: # 중간노드 삽입
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    # current.likt == None까지 오면(마지막)
    node = Node()
    node.data = insertData
    current.link = node
    return


# 노드삭제
def deletNode(deletData):
    global memory, pre, current, head

    if head.data == deletData: # 첫번째 노드 삭제
        current = head
        head = head.link # 두번째 노드로 변경
        del(current)
        return
    
    current = head
    while current.link != None: # 첫번째 이외 노드 삭제
        pre = current   # 모두 첫번째 노드 가리킴
        current = current.link  # 두번째 노드 가리킴
        if current.data == deletData:
            pre.link = current.link # current가 가리키는 노드를 pre 가 가리키도록 하는 것
            del(current)
            return

# 노드 검색
def findNode(findData):
    global memory, pre, current, head

    current = head # 첫번재 노드
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link # 다음 노드
        if current.data == findData:
            return current
    return Node()   # 빈 노드 반환

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0] #첫번째 노드
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두번째 노드 이후부터
        pre = node
        node = Node()
        node.data = data # 기현 형원 주헌 창균 순으로
        pre.link = node
        memory.append(node)

    printNodes(head)    # 전체출력

    print('노드 추가 ----')

    insertNode('민혁', '현우') # 맨 앞에 셔누 노드 추가
    printNodes(head)

    insertNode('창균', '균주') # 중간 노드 추가
    printNodes(head)

    insertNode('여주', '뽀삐') # 없는 노드 앞에 추가한다고 하면 맨 마지막 노드 추가됨
    printNodes(head)


    print('노드 삭제 ----')

    deletNode('뽀삐')
    printNodes(head)

    deletNode('균주')
    printNodes(head)
    
    deletNode('여주') # 없는 데이터라 삭제 안됨
    printNodes(head)


    print('노드 검색 -----')
    result = findNode('기현')
    if result.data != None:
        print(f'{result.data} 데이터 찾았습니다')
    else:
        print('검색한 데이터 없습니다.')

    result = findNode('여주')
    if result.data != None:
        print(f'{result.data} 데이터 찾았습니다')
    else:
        print('검색한 데이터 없습니다.')