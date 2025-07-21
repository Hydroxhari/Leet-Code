# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, h):

        if not h or not h.next:
            return h
        
        ce=h
        co=h.next
        oh=co

        while co.next:
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


