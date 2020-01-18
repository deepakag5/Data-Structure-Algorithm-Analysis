def addTwoNumbersII(l1, l2):
    if not l1 and not l2:
        return ListNode(0)
    elif not l1:
        return l2
    elif not l2:
        return l1

    num1 = l1.val
    num2 = l2.val
    l1 = l1.next
    l2 = l2.next

    while l1 or l2:
        if l1:
            num1 *= 10
            num1 += l1.val
            l1 = l1.next

        if l2:
            num2 *= 10
            num2 += l2.val
            l2 = l2.next

    result = num1 + num2
    if result == 0:
        return ListNode(0)
    next = None

    while result > 0:
        digit = result % 10
        result = result // 10
        node = ListNode(digit)
        if not next:
            next = node
            node.next = None
        else:
            node.next = next
            next = node

    return node
