class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
