# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, head):
        
        # code here
        curr=head
        prev=None
        while curr:
            if curr.prev and curr.prev.data==curr.data:
                if curr.prev==head:
                    curr.prev=None
                    head=curr
                else:
                    curr.prev.prev.next=curr
                    curr.prev=curr.prev.prev
            curr=curr.next
        return head
                
                
            
                