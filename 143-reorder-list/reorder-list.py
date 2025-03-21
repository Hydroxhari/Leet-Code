class Solution(object):
    def reorderList(self, l1):

        f=s=l1
        while f and f.next:
            s=s.next
            f=f.next.next
        l2=s.next
        s.next=None

        c=l2
        p=None
        while c:
            n=c.next
            c.next=p
            p=c
            c=n
        l2=p

        c1,c2=l1,l2
        while c2:
            t1,t2=c1.next,c2.next
            c1.next=c2
            c2.next=t1
            c1,c2=t1,t2
            

        