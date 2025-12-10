def insertNodeAtHead(llist, data):
    # Write your code here
    dummy = SinglyLinkedListNode(data)
    dummy.next = llist
    return dummy
    