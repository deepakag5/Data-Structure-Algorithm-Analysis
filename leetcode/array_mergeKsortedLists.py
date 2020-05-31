# Time: O(N logk) where k is the number of linked lists
# We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
# Sum up the merge process and we can get: O(Nlogk)

# Space : O(1)
# We are not using any extra space just doing it in-place

# define singly linked list
class ListNode:
    def __init__(self):
        self.val = val
        self.next = None


def mergerKSortedLists(lists):
    # edge cases
    if len(lists) == 0:
        return None
    if len(lists) == 1:
        return lists[0]

    num_lists = len(lists)
    interval = 1

    while num_lists > interval:
        for i in range(0, num_lists - interval, interval * 2):
            lists[i] = merge2SortedLists(lists[i], lists[i + interval])
            interval *= 2
    return lists[0] if num_lists > 0 else lists


def merge2SortedLists(l1, l2):
    # edge cases
    if not l1 and not l2:
        return None
    if not l1:
        return l2
    if not l2:
        return l1

    # create pointers to hold the final merged list
    head = curr = ListNode(0)

    # if both l1 and l2 are not empty
    while l1 and l2:
        # if val in l1 is less than l2 then give ref to curr and move forward else vice versa
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        # move curr forward for next values from l1 and l2
        curr = curr.next

    # if l1 or l2 still has items give the ref to curr
    if not l1:
        curr.next = l2
    else:
        curr.next = l1

    # return head pointer (curr holds all the item but its pointer is at last item right now !)
    return head.next
