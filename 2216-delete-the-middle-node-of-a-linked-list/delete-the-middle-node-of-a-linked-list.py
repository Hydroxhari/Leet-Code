# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, h):

        s=f=h
        p=None

        while f and f.next:
            p=s
            s=s.next
            f=f.next.next
        if p:
            p.next=s.next
        else:
            return h.next
        return h