# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head 

        curr = head
        after = curr
        before = None

        while curr != None: 
            if curr.next == None: 
                curr.next = before
                break
            after = curr.next 
            curr.next = before 
            before = curr 
            curr = after

        return curr

        
    

        
      

        
        
        
