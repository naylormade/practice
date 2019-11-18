# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    listy = []
    while l1:
        listy.append(l1.val)
        l1 = l1.next
    while l2:
        listy.append(l2.val)
        l2 = l2.next
    if not listy:
        return
    listy.sort()
    #print(listy)
    listnodes = [ListNode(x) for x in listy[::-1]]
    for i in range(1, len(listnodes)):
        listnodes[i].next = listnodes[i - 1]
    return listnodes[-1]

mergeTwoLists([1,2,4],[1,3,4])