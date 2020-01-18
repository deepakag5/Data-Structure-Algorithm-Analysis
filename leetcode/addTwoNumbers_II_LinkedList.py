def addTwoNumbersII(l1, l2):
    if not l1 and not l2:
        return ListNode(0)
    elif not l1:
        return l2
    elif not l2:
        return l1

    s1 = 0
    s2 = 0

    while l1:
        s1 *= 10
        s1 += l1.val
        l1 = l1.next
    while l2:
        s2 *= 10
        s2 += l2.val
        l2 = l2.next

    s3 = s1 + s2

    if s3 == 0:
        return ListNode(0)

    tail = None
    head = None

    while s3 > 0:
        head = ListNode(s3 % 10)
        head.next = tail
        tail = head
        s3 = s3 // 10

    return head if head else ListNode(0)

# while result>0:
#         node = ListNode(result % 10)
#         result = result // 10
#         if not next:
#             next = node
#             node.next = None
#         else:
#             node.next = next
#             next = node
#
#
#     return node
