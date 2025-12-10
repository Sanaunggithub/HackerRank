def has_cycle(head):    
    if head.next is None or head is None:
        return 0
    
    seen = set()   
    cur = head
    
    while cur:
        if cur in seen:
            return 1          
        seen.add(cur)            
        cur = cur.next        
    return 0