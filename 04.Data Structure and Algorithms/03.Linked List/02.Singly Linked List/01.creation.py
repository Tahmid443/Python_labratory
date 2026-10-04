class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# manually creating a linked list
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)

# node1.next = node2
# node3.next = node3

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

ll = LinkedList()
node1 = Node(10)
node2 = Node(20)
ll.head = node1
ll.head.next = node2
ll.tail = node2