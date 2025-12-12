def deleteNode(llist, position):
   
    # deleting head node
    if position == 0:
        return llist.next
        
    curr = llist
    
    while position > 1:
        curr = curr.next
        position -= 1
        
    curr.next = curr.next.next
    
    return llist