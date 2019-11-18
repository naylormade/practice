# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    listy = []
    head1 = l1.val
    head2 = l2.val
    tail1 = head1
    tail2 = head2
    count = 1

    while l1.next > 0:
        listy.append(l1.val)
    while l2.next > 0:
        listy.append(l2.val)
    listy.sort()
    print(listy)
    # while count < max(len(l1), len(l2)):
    #     print(head)
    #     tail1.next = l1.next
    #     tail2.next = l2.next
    #     if 
    #     tail = tail.next
    #     count += 1
    return listy

mergeTwoLists([1,2,4],[1,3,4])