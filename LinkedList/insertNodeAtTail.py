def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)

    # Case 1: empty list
    if head is None:
        return new_node

    curr = head
    # stop at the last node
    while curr.next is not None:
        curr = curr.next

    curr.next = new_node
    return head
