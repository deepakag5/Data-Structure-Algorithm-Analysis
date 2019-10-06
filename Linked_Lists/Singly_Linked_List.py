class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None


class LinkedList(object):

    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self, node):
        if self.length == 0:
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

        while current.next != None:
            current = current.next

        current.next = newNode
        self.length += 1

    def addAtPos(self, pos, node):
        current = self.head
        prev = self.head
        count = 0

        if pos < 0 or pos > self.length:
            print("Please enter valid pos")
        else:
            while current.next != None or count < pos:
                count += 1

                if count == pos:
                    prev.next = node
                    node.next = current
                    self.length += 1
                    return
                else:
                    prev = current
                    current = current.next

    def addAfterValue(self, data, node):
        newNode = node
        current = self.head

        while current.next != None or current.data != data:
            if current.data == data:
                newNode.next = current.next
                current.next = newNode
                self.length += 1
                return
            else:
                current = current.next

    def deleteBeg(self):
        if self.length == 0:
            print("List is empty")
        else:
            current = self.head
            self.head = current.next
            self.length -= 1

    def deleteLast(self):

        if self.length == 0:
            print("List is empty")
        else:
            current = self.head
            prev = self.head

            while current.next != None:
                prev = current
                current = current.next

            prev.next = None
            self.length -= 1

    def deletAtPos(self, pos):
        count = 0

        current = self.head
        prev = self.head

        if self.length == 0:
            print("Empty List")
        elif self.length == 1:
            self.deleteBeg()
        else:
            while current.next != None or count < pos:
                count += 1

                if count == pos:
                    prev.next = current.next
                    self.length -= 1
                    return

                else:
                    prev = current
                    current = current.next

    def deleteVal(self, data):

        prev = self.head
        current = self.head

        if self.length == 0:
            print("Empty List")
        elif self.length == 1:
            self.deleteBeg()
        else:

            while current.next != None or current.data != data:
                if current.data == data:
                    prev.next = current.next
                    self.length -= 1
                    return

                else:
                    prev = current
                    current = current.next

    def getLength(self):
        return self.length

    def getFirst(self):
        if self.length == 0:
            print("List Empty")
        else:
            return self.head.data

    def getLast(self):
        if self.length == 0:
            print("List Empty")
        else:
            current = self.head

            while current.next != None:
                current = current.next

            return current.data

    def getAtPos(self, pos):
        count = 0

        current = self.head

        if pos < 0 or pos > self.length:
            print("Please enter valid pos")
        else:
            while current.next != None or count < pos:
                if count == pos:
                    return current.data
                else:
                    current = current.next

    def print_list(self):
        nodeList = []
        current = self.head

        while current != None:
            nodeList.append(current.data)
            current = current.next

        print(nodeList)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

ll = LinkedList()

ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)

ll.print_list()
