# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, h):
        l=[]
        c=h
        while c:
            if c in l:
                return True
            l.append(c)
            c=c.next
            
        return False

        