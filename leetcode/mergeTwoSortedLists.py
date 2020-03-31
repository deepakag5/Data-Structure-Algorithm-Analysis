# Time: O(m+n)
# Space: O(m+n)

def mergeRecursive(self, l1, l2):
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l1:
        return l2

    if l1.val < l2.val:
        l1.next = self.merge(l1.next, l2)
        return l1
    else:
        l2.next = self.merge(l1, l2.next)
        return l2


# Iterative Approach Optimized for Space
# Time: O(m+n)
# Space: O(1)

def mergeIterative(self, l1, l2):
    # base cases
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1

    # create pointers to hold the final merged list
    dummy = curr = ListNode(0)

    # if both l1 and l2 are not empty
    while l1 and l2:
        # if val in l1 is less than l2 then give ref to curr and move forward else vice versa
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        # move curr forward for next values from l1 and l2
        curr = curr.next

    # if l1 or l2 still has items give the ref to curr
    if l1:
        curr.next = l1
    else:
        curr.next = l2

    # return head pointer (curr holds all the item but its pointer is at last item right now !)
    return dummy.next
