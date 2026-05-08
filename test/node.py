class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

n1 = Node(10)
n2 = Node(20)
n1.next = n2
print(n1.next.data)

cur = n1
while cur:
    print(cur.data)
    cur = cur.next

cur = head
while cur.next:
    cur = cur.next
print(cur.data)


new_node = Node(5)
new_node.next = head
head = new_node


cur = head
cur = cur.next
new_node = Node(25)
new_node.next = cur.next
cur.next = new_node

cur = head
while cur.next:
    cur = cur.next
cur.next = Node(40)

def find(head, target):
    cur = head
    while cur:
        if cur.data == target:
            return True
        cur = cur.next
    return False