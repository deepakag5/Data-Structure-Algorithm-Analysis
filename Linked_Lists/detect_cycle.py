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

        current = self.head

        while current is not None:
            nodeList.append(current.data)
            current = current.next

        print(nodeList)

    def detectCycle(self):
        fast_p = self.head
        slow_p = self.head

        while fast_p and slow_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                return True

    def detectCycleStart(self):
        if self.head == None or self.head.next == None:
            return None
        slow = self.head.next
        fast = slow.next

        while slow != fast:
            slow = slow.next
            try:
                fast = fast.next.next
            except AttributeError:
                return None

        slow = self.head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


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

# create a loop for detecting cycle
ll.head.next.next.next.next.next = ll.head

# will print True if there is cycle in linked list
print(ll.detectCycle())

# print the node where the loop starts if cycle exists
print(ll.detectCycleStart().get_data())
