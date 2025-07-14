# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, h):

        c=h
        s=''
        while c:
            s+=str(c.val)
            c=c.next
        return int(s,2)
