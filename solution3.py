def mergeSortedList(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data < head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next

    current_node = head
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            current_node.next = head1
            head1 = head1.next
        else:
            current_node.next = head2
            head2 = head2.next
        current_node = current_node.next

    if head1 is not None:
        current_node.next = head1
    else:
        current_node.next = head2

    return head














'''
def mergeSortedList(h1, h2):
    h3 = Node()
    L = []
    while h1 != None:
        L.append(h1.data)
        h1 = h1.next
    while h2 != None:
        L.append(h2.data)
        h2 = h2.next
    print(*sorted(L))    
    
'''