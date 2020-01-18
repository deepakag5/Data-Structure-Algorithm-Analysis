def reverseLL(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        if not next_node:
            return head
        prev = curr
        curr = next_node

    return prev
