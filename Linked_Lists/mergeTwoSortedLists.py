from Singly_Linked_List import Node, LinkedList


# create a new class which will inherit the methods of the base class of LinkedList
class Linked_List(LinkedList):

    def mergeTwoSortedLL(self, list1, list2):
        temp = Node(0)

        while list1 is not None and list2 is not None:
            if list1.get_data() < list2.get_data():
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

        if list1 is None:
            temp.next = list2
        else:
            temp.next = list1

        return temp.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# create linked list object
ll1 = Linked_List()

# add nodes to linked list
ll1.addNode(node1)
ll1.addNode(node2)
ll1.addNode(node3)

node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

# create linked list object
ll2 = Linked_List()

# add nodes to linked list
ll2.addNode(node4)
ll2.addNode(node5)
ll2.addNode(node6)

ll1.print_list()
ll2.print_list()

ll3 = Linked_List()

print(ll3.mergeTwoSortedLL(ll1.head, ll2.head))
