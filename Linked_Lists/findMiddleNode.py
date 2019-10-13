from Singly_Linked_List import Node, LinkedList


# create a new class which will inherit the methods of the base class of LinkedList
class Linked_List(LinkedList):

    def findMiddle(self):
        fast_p = self.head
        slow_p = self.head

        # we will take two pointers, the fast pointer will reach either NoneType when we increment by 2 places
        # at that time the slow ptr will be at exactly middle of the linked list
        while fast_p is not None:
            fast_p = fast_p.next

            if fast_p is None:
                return slow_p

            fast_p = fast_p.next
            slow_p = slow_p.next

        return slow_p


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

# reverse the list in place
print(ll.findMiddle().get_data())
