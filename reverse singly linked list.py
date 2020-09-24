    prev=None
    cur=head    
    nxt=None
    while cur:
        nxt=cur.next
        cur.next=prev
        prev=cur
        cur=nxt
    head=prev
    return head
