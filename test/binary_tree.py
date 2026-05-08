class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(20)
root.left = Node(10)
root.right = Node(30)

print(root.right.data) #30
print(root.left.data) #10

def preorder(node): #전위 순회 (루트 -> 왼쪽 -> 오른쪽)
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def inorder(node): #중위 순회 (왼쪽 -> 루트 -> 오른쪽)
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def postorder(node): #후위 순회 (왼쪽 -> 오른쪽 -> 루트)
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
        
def count_nodes(node):
    if node is None:
        return 0
    #현재 노드 1개 + 왼쪽 서브트리 개수 + 오른쪽 서브트리 개수
    return 1 + count_nodes(node.left) + count_nodes(node.right)