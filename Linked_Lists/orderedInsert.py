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
            current = current, next

        current.next = newNode
        self.length += 1

    def printList(self):
        nodeList = []

        current = self.head
        while current is not None:
            nodeList.append(current.data)
            current = current.next

        print(nodeList)
