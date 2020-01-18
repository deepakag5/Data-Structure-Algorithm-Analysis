# Time: O(n)
# Space: O(n)

def detectCycleList(head):
    seen_list = []

    while head is not None:
        if head in seen_list:
            return True
        else:
            seen_list.append(head)

        head = head.next

    return False


# Optimized for Space
# Time: O(n)
# Space: O(1)

def detectCycleTwoPointers(head):
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True
