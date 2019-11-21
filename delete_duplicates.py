def deleteDuplicates(head):
    listy = []
    if not head: return head
    while head:
        if head.val not in listy:
            listy.append(head.val)
        head = head.next
    listnodes = [ListNode(x) for x in listy[::-1]]
    for i in range(1, len(listnodes)):
        listnodes[i].next = listnodes[i - 1]
    return listnodes[-1]