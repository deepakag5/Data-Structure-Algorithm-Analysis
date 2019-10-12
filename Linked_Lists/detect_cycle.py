from Singly_Linked_List import Node


class Linked_List:

    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self, node):
        if self.head is None:
            self.addBeg(node)
        else:
            self.addLast(node)

    def addBeg(self, node):
        newNode = node
        newNode.next = self.head

        self.head = newNode
        self.length += 1

    def addLast(self, node):
        newNode = node
        newNode.next = None

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = newNode
        self.length += 1

    def print_list(self):
        nodeList = []

        while
