# 이진 탐색 트리 구현

# 전역변수 선언
memory = []
root = None
nameAry = ['셔누', '민혁', '기현', '주헌', '아이엠', '형원']

class TreeNode:
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

if __name__ == '__main__':
    node = TreeNode()
    node.data = nameAry[0]
    root = node
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name

        current = root

        while True:
            if name < current.data: # 부모노드 왼쪽으로
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else:   # 부모노드 오른쪽으로
                if current.right == None:
                    current.right = node
                    break
                current = current.right
        
        memory.append(node)
    
    print('이진트리 탐색 종료')

    print(root.data)
    print('｜      ＼')
    print(root.left.data, '  ',root.right.data)
    print('｜      ｜    ＼              ')
    print(root.left.left.data, '',root.right.left.data, '  ',root.right.right.data)


    search = input('찾을 멤버를 입력 > ')

    current = root
    while True:
        if search == current.data:
            print(search, '찾음 끝!')
            break
        elif search < current.data: #왼쪽으로
            if current.left == None:
                print(search, '못찾음 끝!')
                break
            else:
                current= current.left
        else:   #오른쪽으로
            if current.right == None:
                print(search, '못찾음 끝!')
                break
            else:
                current = current.right