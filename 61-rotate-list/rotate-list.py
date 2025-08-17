class Solution(object):
    def rotateRight(self, h, k):

        if not h or k==0 or not h.next:
            return h

        l=0
        c=h
        while c:
            l+=1
            c=c.next
        
        r = l - (k%l)
        if r==l:
            return h

        p=None
        c=h
        while r:
            r-=1
            p=c
            c=c.next
        
        p.next=None
        ch=c
        while c.next:
            c=c.next
        c.next=h

        return ch