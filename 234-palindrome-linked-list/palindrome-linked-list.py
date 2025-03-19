# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, h):
        c=h
        l=[]
        while h:
            l.append(h.val)
            h=h.next
        return l==l[::-1]
