from Singly_Linked_List import Node


class Linked_List:

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

        while current.next is not None:
            current = current.next

        current.next = newNode
        self.length += 1

    # print linked list data
    def print_list(self):
        nodeList = []
        current = self.head

        while current != None:
            nodeList.append(current.data)
            current = current.next

        print(nodeList)

    def nth_node_from_end(self, n):
        if n < 0:
            return None

        length = 0
        temp = self.head

        while temp is not None:
            temp = temp.next
            length += 1

        if n > length:
            print("Number of nodes in LL is less than specified n")

        current = self.head

        for i in range(0, length - n):
            current = current.next

        print(current.data)

    def nth_node_from_end_twoPtr(self, n):
        current = self.head
        nth = self.head

        count = 0
        if self.head is not None:
            while count < n:
                if current is None:
                    print("n is greater than number of nodes in the list")

                current = current.next
                count += 1

        while current is not None:
            current = current.next
            nth = nth.next

        print(nth.data)




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

# print linked list
ll.print_list()

# print nth node from end of linked list
ll.nth_node_from_end(4)

ll.nth_node_from_end_twoPtr(4)
