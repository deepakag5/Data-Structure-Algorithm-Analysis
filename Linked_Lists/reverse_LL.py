from Singly_Linked_List import Node


class Linked_List:

    def __init__(self):
        self.head = None
        self.length = 0

    def addNode(self, node):
        if self.head == None:
            self.addBeg(node)
        else:
            self.addLast(node)

    def addBeg(self, node):
        newNode = node

        newNode.next = self.head
        self.head = node

        self.length += 1

    def addLast(self, node):
        newNode = node
        newNode.next = None

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = newNode
        self.length += 1

    def printList(self):
        nodeList = []

        current = self.head
        while current is not None:
            nodeList.append(current.data)
            current = current.next

        print(nodeList)

    def rev_LL(self):
        prevNode = None
        nextNode = None
        current = self.head

        while current is not None:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode

        self.head = prevNode


# specify the nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# create linked list object
ll = Linked_List()

# add nodes to linked list
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)

# print the list
ll.printList()

# reverse the list in place
ll.rev_LL()

# print the updated list
ll.printList()
