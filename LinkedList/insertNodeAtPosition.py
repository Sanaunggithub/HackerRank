def insertNodeAtPosition(llist, data, position):
    # Write your code here
    dummy = SinglyLinkedListNode(data)
    
    curr = llist
    
    while position > 1:
        curr = curr.next
        position -= 1
    dummy.next = curr.next
    curr.next = dummy
    return llist