# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, h):

        if not h:
            return h
        
        ce=h
        co=h.next
        oh=h.next
        im=False

        while co and co.next:
            if co.next:
                ce.next=co.next
                ce=ce.next

            if ce.next:
                co.next=ce.next
                co=co.next
            else:
                co.next=None
            
        ce.next=oh
    
        return h


