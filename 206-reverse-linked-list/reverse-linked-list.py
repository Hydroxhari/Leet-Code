# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, h):

        c=h
        p=None

        while c:
            n=c.next
            c.next=p
            p=c
            c=n

        return p

