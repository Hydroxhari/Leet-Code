class Solution(object):
    def sortList(self, h):
        c=h
        l=[]
        while c:
            l.append(c.val)
            c=c.next
        l.sort()
        n=ListNode()
        c=n
        for i in l:
            c.next=ListNode(i)
            c=c.next
        return n.next