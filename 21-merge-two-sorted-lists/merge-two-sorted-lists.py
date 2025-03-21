# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l=ListNode(0)
        c=l
        while l1 and l2:
            if l1.val>l2.val:
                c.next=l2
                l2=l2.next
            else:
                c.next=l1
                l1=l1.next
            c=c.next
        if l1:
            c.next=l1
        if l2:
            c.next=l2
        return l.next


        