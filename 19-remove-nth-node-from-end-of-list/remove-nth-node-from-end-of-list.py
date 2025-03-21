class Solution(object):
    def removeNthFromEnd(self, h, n):
        c=h
        l=0
        while c:
            l+=1
            c=c.next
        l=l-n

        nh=ListNode(0)
        nh.next=h
        c=nh
        while l>0:
            c=c.next
            l-=1
        c.next=c.next.next
        return nh.next

        