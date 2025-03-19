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

        