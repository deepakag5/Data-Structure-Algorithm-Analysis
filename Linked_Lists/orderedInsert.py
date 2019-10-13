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

    def orderdIns(self, item):
        current = self.head
        stop = False
        prev = None

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                prev = current
                current = current.next

        temp = Node(item)

        # check if there is only one node present then it's same as insert at beg
        if prev is None:
            temp.next = self.head
            self.head = temp
            self.length += 1
        # otherwise it's same as inserting the node at specific position
        else:
            prev.next = temp
            temp.next = current
            self.length += 1


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

# add one node at last
ll.orderdIns(6)

# add one node at begining
ll.orderdIns(0)

# add one node in between
ll.orderdIns(2.5)

# print the updated list
ll.printList()
