# Time: O(N) = O(N) , N/2, N/2
# Space: O(1)


def reorder_ll(head):
    if not head:
        return

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first, second = head, prev

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
