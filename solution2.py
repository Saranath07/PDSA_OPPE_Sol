def removeDuplicate(head):
    if head is None:
        return head

    temp = head
    while temp.next is not None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next

    return head